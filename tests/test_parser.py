from bluetooth_sensor_state_data import DeviceClass, SensorUpdate
from home_assistant_bluetooth import BluetoothServiceInfo
from sensor_state_data import (
    DeviceKey,
    SensorDescription,
    SensorDeviceInfo,
    SensorValue,
    Units,
)

from aicooking_ble.parser import ERROR, AicookingBluetoothDeviceData


def test_can_create():
    """Test parser instantiation."""
    AicookingBluetoothDeviceData()


def test_bbq():
    """Test parsing a valid BBQ advertisement."""
    parser = AicookingBluetoothDeviceData()
    service_info = BluetoothServiceInfo(
        name="BBQ",
        manufacturer_data={21930: b"21.1"},
        service_uuids=["0000180a-0000-1000-8000-00805f9b34fb"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        service_data={},
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="BBQ",
                model="CXL001-Y",
                manufacturer="Aicooking",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=DeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=DeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=21.1,
            ),
        },
    )


def test_no_manufacturer_data():
    """Test advertisement with no manufacturer data is ignored."""
    parser = AicookingBluetoothDeviceData()
    service_info = BluetoothServiceInfo(
        name="BBQ",
        manufacturer_data={},
        service_uuids=["0000180a-0000-1000-8000-00805f9b34fb"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        service_data={},
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None, devices={}, entity_descriptions={}, entity_values={}
    )


def test_invalid_temperature_low():
    """Test temperature below MIN_TEMP results in error state."""
    parser = AicookingBluetoothDeviceData()
    service_info = BluetoothServiceInfo(
        name="BBQ",
        manufacturer_data={21930: b"-20."},
        service_uuids=["0000180a-0000-1000-8000-00805f9b34fb"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        service_data={},
        source="local",
    )
    result = parser.update(service_info)
    assert (
        result.entity_values[DeviceKey(key="temperature", device_id=None)].native_value
        == ERROR
    )


def test_invalid_temperature_high():
    """Test temperature above MAX_TEMP results in error state."""
    parser = AicookingBluetoothDeviceData()
    service_info = BluetoothServiceInfo(
        name="BBQ",
        manufacturer_data={21930: b"301."},
        service_uuids=["0000180a-0000-1000-8000-00805f9b34fb"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        service_data={},
        source="local",
    )
    result = parser.update(service_info)
    assert (
        result.entity_values[DeviceKey(key="temperature", device_id=None)].native_value
        == ERROR
    )


def test_unsupported_device():
    """Test advertisement from unsupported device is ignored."""
    parser = AicookingBluetoothDeviceData()
    service_info = BluetoothServiceInfo(
        name="OtherName",
        manufacturer_data={1234: b"25.0"},
        service_uuids=[],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        service_data={},
        source="local",
    )
    result = parser.update(service_info)
    # The manufacturer id 1234 and name OtherName are not processed,
    # so no temperature or signal_strength sensor value
    assert DeviceKey(key="temperature", device_id=None) not in result.entity_values


def test_switched_adapters():
    """Test advertisement when multiple adapters send data is ignored."""
    parser = AicookingBluetoothDeviceData()
    service_info = BluetoothServiceInfo(
        name="BBQ",
        manufacturer_data={21930: b"21.1"},
        service_uuids=["0000180a-0000-1000-8000-00805f9b34fb"],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        service_data={},
        source="local",
    )
    from unittest.mock import patch

    with patch.object(
        parser, "changed_manufacturer_data", return_value={1: b"data1", 2: b"data2"}
    ):
        result = parser.update(service_info)
    assert DeviceKey(key="temperature", device_id=None) not in result.entity_values
