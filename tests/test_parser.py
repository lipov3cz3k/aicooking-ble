from bluetooth_sensor_state_data import BluetoothServiceInfo, DeviceClass, SensorUpdate
from sensor_state_data import (
    DeviceKey,
    SensorDescription,
    SensorDeviceInfo,
    SensorValue,
    Units,
)

from aicooking_ble.parser import AicookingBluetoothDeviceData


def test_can_create():
    AicookingBluetoothDeviceData()


def test_bbq():
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
