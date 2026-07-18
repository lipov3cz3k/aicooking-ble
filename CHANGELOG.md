# CHANGELOG

## v0.2.1 (2026-07-18)

### Fix

* fix(ci): add PyPI publish step after semantic-release

The semantic-release action only creates GitHub releases but does not
publish to PyPI. Added pypa/gh-action-pypi-publish with OIDC trusted
publisher to automatically upload built artifacts to PyPI when a new
version is released. ([`b4b17c2`](https://github.com/lipov3cz3k/aicooking-ble/commit/b4b17c2f259ed54094807c2939973759cb77d5d2))

### Unknown

* Merge pull request #106 from lipov3cz3k/fix/pypi-publish

fix(ci): add PyPI publish step after semantic-release ([`3e1432e`](https://github.com/lipov3cz3k/aicooking-ble/commit/3e1432e5ace8cf639d7cbc2d97321fd1feec275c))

## v0.2.0 (2026-07-18)

### Chore

* chore(ci): switch PyPI publishing to Trusted Publisher OIDC ([`7344730`](https://github.com/lipov3cz3k/aicooking-ble/commit/7344730e01f264b326885868f2a52c42b3722ae4))

* chore(deps): update dependency lock file ([`c015f7c`](https://github.com/lipov3cz3k/aicooking-ble/commit/c015f7ce09be05b7edb51bdd4ae64c45ab314db1))

* chore(project): configure ruff and remove old isort config in pyproject.toml ([`a638750`](https://github.com/lipov3cz3k/aicooking-ble/commit/a63875052e1e1b81f440b0d1c2db648fc4723732))

* chore(project): modernize pre-commit configuration using ruff ([`a464dc4`](https://github.com/lipov3cz3k/aicooking-ble/commit/a464dc4b65b0ee3af051ae7128242b430c7c6075))

* chore(commitlint): rename config file to .cjs for ESM compatibility ([`f4afe0f`](https://github.com/lipov3cz3k/aicooking-ble/commit/f4afe0f50993a8d72d5c34bea7df9d45a93e8205))

* chore(ci): update Python versions in lint job and test matrix ([`412354d`](https://github.com/lipov3cz3k/aicooking-ble/commit/412354dd5f3cced43138e89e1c8530e73e4057f3))

* chore(project): migrate pyproject.toml to PEP 621 format and update dependencies ([`87337ce`](https://github.com/lipov3cz3k/aicooking-ble/commit/87337ce32f462e7c505827a695319a1bdda116ff))

* chore(deps): bump wagoid/commitlint-github-action from 5.4.5 to 6.2.1

Bumps [wagoid/commitlint-github-action](https://github.com/wagoid/commitlint-github-action) from 5.4.5 to 6.2.1.
- [Changelog](https://github.com/wagoid/commitlint-github-action/blob/master/CHANGELOG.md)
- [Commits](https://github.com/wagoid/commitlint-github-action/compare/v5.4.5...v6.2.1)

---
updated-dependencies:
- dependency-name: wagoid/commitlint-github-action
  dependency-version: 6.0.1
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`25125ce`](https://github.com/lipov3cz3k/aicooking-ble/commit/25125ce5e7d476fd5c5253e267571be93ab212bc))

* chore(deps): bump relekang/python-semantic-release from 9.4.0 to 9.8.3

Bumps [relekang/python-semantic-release](https://github.com/relekang/python-semantic-release) from 9.4.0 to 9.8.3.
- [Release notes](https://github.com/relekang/python-semantic-release/releases)
- [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
- [Commits](https://github.com/relekang/python-semantic-release/compare/v9.4.0...v9.8.3)

---
updated-dependencies:
- dependency-name: relekang/python-semantic-release
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`92bc2c4`](https://github.com/lipov3cz3k/aicooking-ble/commit/92bc2c4bd01b16a37352449b9006069cfa311f21))

* chore(deps-dev): bump pytest from 8.1.1 to 8.2.2

Bumps [pytest](https://github.com/pytest-dev/pytest) from 8.1.1 to 8.2.2.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/8.1.1...8.2.2)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`22c8092`](https://github.com/lipov3cz3k/aicooking-ble/commit/22c80926b08ec7ca5b37a8e714dc90f2dce099ce))

* chore(deps): bump relekang/python-semantic-release from 9.1.1 to 9.4.0

Bumps [relekang/python-semantic-release](https://github.com/relekang/python-semantic-release) from 9.1.1 to 9.4.0.
- [Release notes](https://github.com/relekang/python-semantic-release/releases)
- [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
- [Commits](https://github.com/relekang/python-semantic-release/compare/v9.1.1...v9.4.0)

---
updated-dependencies:
- dependency-name: relekang/python-semantic-release
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`44a97fa`](https://github.com/lipov3cz3k/aicooking-ble/commit/44a97fab49e550ee2e86690f3d576d735df3df74))

* chore(deps): bump bluetooth-sensor-state-data from 1.6.1 to 1.6.2

Bumps [bluetooth-sensor-state-data](https://github.com/bluetooth-devices/bluetooth-sensor-state-data) from 1.6.1 to 1.6.2.
- [Release notes](https://github.com/bluetooth-devices/bluetooth-sensor-state-data/releases)
- [Changelog](https://github.com/Bluetooth-Devices/bluetooth-sensor-state-data/blob/main/CHANGELOG.md)
- [Commits](https://github.com/bluetooth-devices/bluetooth-sensor-state-data/compare/v1.6.1...v1.6.2)

---
updated-dependencies:
- dependency-name: bluetooth-sensor-state-data
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f1405bd`](https://github.com/lipov3cz3k/aicooking-ble/commit/f1405bdbf6d10639be4b9a8e567a7ac50d566dda))

* chore(deps): bump sensor-state-data from 2.17.1 to 2.18.0

Bumps [sensor-state-data](https://github.com/bluetooth-devices/sensor-state-data) from 2.17.1 to 2.18.0.
- [Release notes](https://github.com/bluetooth-devices/sensor-state-data/releases)
- [Changelog](https://github.com/Bluetooth-Devices/sensor-state-data/blob/main/CHANGELOG.md)
- [Commits](https://github.com/bluetooth-devices/sensor-state-data/compare/v2.17.1...v2.18.0)

---
updated-dependencies:
- dependency-name: sensor-state-data
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0d36726`](https://github.com/lipov3cz3k/aicooking-ble/commit/0d36726d290e7665a4dbe325481438cdc2d4ddde))

* chore(deps): bump home-assistant-bluetooth from 1.10.3 to 1.10.4

Bumps [home-assistant-bluetooth](https://github.com/home-assistant-libs/home-assistant-bluetooth) from 1.10.3 to 1.10.4.
- [Release notes](https://github.com/home-assistant-libs/home-assistant-bluetooth/releases)
- [Changelog](https://github.com/home-assistant-libs/home-assistant-bluetooth/blob/main/CHANGELOG.md)
- [Commits](https://github.com/home-assistant-libs/home-assistant-bluetooth/compare/v1.10.3...v1.10.4)

---
updated-dependencies:
- dependency-name: home-assistant-bluetooth
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7d4474a`](https://github.com/lipov3cz3k/aicooking-ble/commit/7d4474ac6e9d8a5d625b60216ea0eebfd4dded20))

* chore(deps-dev): bump pytest from 7.4.3 to 8.1.1

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.3 to 8.1.1.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.4.3...8.1.1)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`5468f02`](https://github.com/lipov3cz3k/aicooking-ble/commit/5468f02d6e9523be1f47a49f3fd6fd6f7a341a1c))

* chore(deps): bump relekang/python-semantic-release from 8.5.1 to 9.1.1

Bumps [relekang/python-semantic-release](https://github.com/relekang/python-semantic-release) from 8.5.1 to 9.1.1.
- [Release notes](https://github.com/relekang/python-semantic-release/releases)
- [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
- [Commits](https://github.com/relekang/python-semantic-release/compare/v8.5.1...v9.1.1)

---
updated-dependencies:
- dependency-name: relekang/python-semantic-release
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7848591`](https://github.com/lipov3cz3k/aicooking-ble/commit/78485911fd6d3a94a4973409e17ecb84e9f230aa))

* chore(deps): bump pre-commit/action from 3.0.0 to 3.0.1

Bumps [pre-commit/action](https://github.com/pre-commit/action) from 3.0.0 to 3.0.1.
- [Release notes](https://github.com/pre-commit/action/releases)
- [Commits](https://github.com/pre-commit/action/compare/v3.0.0...v3.0.1)

---
updated-dependencies:
- dependency-name: pre-commit/action
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ce5aee8`](https://github.com/lipov3cz3k/aicooking-ble/commit/ce5aee8c8c9d3d4a730747bdfe0adbca9d5fa953))

* chore(deps): bump tiangolo/issue-manager from 0.4.0 to 0.5.0

Bumps [tiangolo/issue-manager](https://github.com/tiangolo/issue-manager) from 0.4.0 to 0.5.0.
- [Release notes](https://github.com/tiangolo/issue-manager/releases)
- [Commits](https://github.com/tiangolo/issue-manager/compare/0.4.0...0.5.0)

---
updated-dependencies:
- dependency-name: tiangolo/issue-manager
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`90ae1ad`](https://github.com/lipov3cz3k/aicooking-ble/commit/90ae1ad0cf1f392677f8cb6bc2969362d1963af8))

* chore(deps): bump codecov/codecov-action from 3 to 4

Bumps [codecov/codecov-action](https://github.com/codecov/codecov-action) from 3 to 4.
- [Release notes](https://github.com/codecov/codecov-action/releases)
- [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md)
- [Commits](https://github.com/codecov/codecov-action/compare/v3...v4)

---
updated-dependencies:
- dependency-name: codecov/codecov-action
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`6d56185`](https://github.com/lipov3cz3k/aicooking-ble/commit/6d56185725ac7221998f4cceab921517af85f2a9))

* chore(deps): bump wagoid/commitlint-github-action from 5.4.4 to 5.4.5

Bumps [wagoid/commitlint-github-action](https://github.com/wagoid/commitlint-github-action) from 5.4.4 to 5.4.5.
- [Changelog](https://github.com/wagoid/commitlint-github-action/blob/master/CHANGELOG.md)
- [Commits](https://github.com/wagoid/commitlint-github-action/compare/v5.4.4...v5.4.5)

---
updated-dependencies:
- dependency-name: wagoid/commitlint-github-action
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`d6dc0d0`](https://github.com/lipov3cz3k/aicooking-ble/commit/d6dc0d0a08e2630a182a5790aa3352dd3db18477))

* chore(deps): bump relekang/python-semantic-release from 8.1.1 to 8.5.1

Bumps [relekang/python-semantic-release](https://github.com/relekang/python-semantic-release) from 8.1.1 to 8.5.1.
- [Release notes](https://github.com/relekang/python-semantic-release/releases)
- [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
- [Commits](https://github.com/relekang/python-semantic-release/compare/v8.1.1...v8.5.1)

---
updated-dependencies:
- dependency-name: relekang/python-semantic-release
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`afb20d1`](https://github.com/lipov3cz3k/aicooking-ble/commit/afb20d17ddb5a44f0dc9c7286accca39ceacffa5))

* chore(deps): bump actions/setup-python from 4 to 5

Bumps [actions/setup-python](https://github.com/actions/setup-python) from 4 to 5.
- [Release notes](https://github.com/actions/setup-python/releases)
- [Commits](https://github.com/actions/setup-python/compare/v4...v5)

---
updated-dependencies:
- dependency-name: actions/setup-python
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`9dcb3f3`](https://github.com/lipov3cz3k/aicooking-ble/commit/9dcb3f369d34ae05add2e2377c10396a88e9d2b0))

* chore(deps-dev): bump sphinx-rtd-theme from 1.3.0 to 2.0.0

Bumps [sphinx-rtd-theme](https://github.com/readthedocs/sphinx_rtd_theme) from 1.3.0 to 2.0.0.
- [Changelog](https://github.com/readthedocs/sphinx_rtd_theme/blob/master/docs/changelog.rst)
- [Commits](https://github.com/readthedocs/sphinx_rtd_theme/compare/1.3.0...2.0.0)

---
updated-dependencies:
- dependency-name: sphinx-rtd-theme
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ff600ab`](https://github.com/lipov3cz3k/aicooking-ble/commit/ff600ab5f2979cf95fcb63368ad7f375532ca0a9))

* chore(deps): bump wagoid/commitlint-github-action from 5.4.3 to 5.4.4

Bumps [wagoid/commitlint-github-action](https://github.com/wagoid/commitlint-github-action) from 5.4.3 to 5.4.4.
- [Changelog](https://github.com/wagoid/commitlint-github-action/blob/master/CHANGELOG.md)
- [Commits](https://github.com/wagoid/commitlint-github-action/compare/v5.4.3...v5.4.4)

---
updated-dependencies:
- dependency-name: wagoid/commitlint-github-action
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`3be55bd`](https://github.com/lipov3cz3k/aicooking-ble/commit/3be55bd76fab1968e0e11784875bded88578ccb3))

* chore(deps-dev): bump pytest from 7.4.2 to 7.4.3

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.2 to 7.4.3.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.4.2...7.4.3)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0509624`](https://github.com/lipov3cz3k/aicooking-ble/commit/0509624ffe95e5853092b29fc5d0463856c28087))

* chore(deps): bump relekang/python-semantic-release from 8.0.4 to 8.1.1

Bumps [relekang/python-semantic-release](https://github.com/relekang/python-semantic-release) from 8.0.4 to 8.1.1.
- [Release notes](https://github.com/relekang/python-semantic-release/releases)
- [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
- [Commits](https://github.com/relekang/python-semantic-release/compare/v8.0.4...v8.1.1)

---
updated-dependencies:
- dependency-name: relekang/python-semantic-release
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`3672d69`](https://github.com/lipov3cz3k/aicooking-ble/commit/3672d6971addd3dd2f4e726fa952ddc3f5a28bba))

* chore(deps): bump actions/checkout from 3 to 4

Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
- [Release notes](https://github.com/actions/checkout/releases)
- [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
- [Commits](https://github.com/actions/checkout/compare/v3...v4)

---
updated-dependencies:
- dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`5f5470f`](https://github.com/lipov3cz3k/aicooking-ble/commit/5f5470f068111493a758f8ee6fb4009f039db391))

* chore(deps-dev): bump myst-parser from 1.0.0 to 2.0.0

Bumps [myst-parser](https://github.com/executablebooks/MyST-Parser) from 1.0.0 to 2.0.0.
- [Release notes](https://github.com/executablebooks/MyST-Parser/releases)
- [Changelog](https://github.com/executablebooks/MyST-Parser/blob/master/CHANGELOG.md)
- [Commits](https://github.com/executablebooks/MyST-Parser/compare/v1.0.0...v2.0.0)

---
updated-dependencies:
- dependency-name: myst-parser
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0d6f8ab`](https://github.com/lipov3cz3k/aicooking-ble/commit/0d6f8ab1bf296d23c90d16a725b6c569893f2fe9))

* chore(deps-dev): bump sphinx from 6.2.1 to 7.2.6

Bumps [sphinx](https://github.com/sphinx-doc/sphinx) from 6.2.1 to 7.2.6.
- [Release notes](https://github.com/sphinx-doc/sphinx/releases)
- [Changelog](https://github.com/sphinx-doc/sphinx/blob/master/CHANGES.rst)
- [Commits](https://github.com/sphinx-doc/sphinx/compare/v6.2.1...v7.2.6)

---
updated-dependencies:
- dependency-name: sphinx
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f0ba57d`](https://github.com/lipov3cz3k/aicooking-ble/commit/f0ba57d04261a0fac496d446621c56a37acfa1de))

* chore(deps-dev): bump sphinx-rtd-theme from 1.2.2 to 1.3.0

Bumps [sphinx-rtd-theme](https://github.com/readthedocs/sphinx_rtd_theme) from 1.2.2 to 1.3.0.
- [Changelog](https://github.com/readthedocs/sphinx_rtd_theme/blob/master/docs/changelog.rst)
- [Commits](https://github.com/readthedocs/sphinx_rtd_theme/compare/1.2.2...1.3.0)

---
updated-dependencies:
- dependency-name: sphinx-rtd-theme
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`21f09bd`](https://github.com/lipov3cz3k/aicooking-ble/commit/21f09bd19b5d7e3ff376cbcf9c3e168a0eebc002))

* chore(deps): bump sensor-state-data from 2.13.0 to 2.17.1

Bumps [sensor-state-data](https://github.com/bluetooth-devices/sensor-state-data) from 2.13.0 to 2.17.1.
- [Release notes](https://github.com/bluetooth-devices/sensor-state-data/releases)
- [Changelog](https://github.com/Bluetooth-Devices/sensor-state-data/blob/main/CHANGELOG.md)
- [Commits](https://github.com/bluetooth-devices/sensor-state-data/compare/v2.13.0...v2.17.1)

---
updated-dependencies:
- dependency-name: sensor-state-data
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`5dbffeb`](https://github.com/lipov3cz3k/aicooking-ble/commit/5dbffebc870aa534851de1b73e91b55a6aa665d5))

* chore(deps): bump home-assistant-bluetooth from 1.9.3 to 1.10.3

Bumps [home-assistant-bluetooth](https://github.com/home-assistant-libs/home-assistant-bluetooth) from 1.9.3 to 1.10.3.
- [Release notes](https://github.com/home-assistant-libs/home-assistant-bluetooth/releases)
- [Changelog](https://github.com/home-assistant-libs/home-assistant-bluetooth/blob/main/CHANGELOG.md)
- [Commits](https://github.com/home-assistant-libs/home-assistant-bluetooth/compare/v1.9.3...v1.10.3)

---
updated-dependencies:
- dependency-name: home-assistant-bluetooth
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`d187e4a`](https://github.com/lipov3cz3k/aicooking-ble/commit/d187e4a0304ea2004996d2411514b5ad8b57a538))

* chore(deps-dev): bump pytest from 7.3.1 to 7.4.2

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.3.1 to 7.4.2.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.3.1...7.4.2)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`3c976fc`](https://github.com/lipov3cz3k/aicooking-ble/commit/3c976fcafb892cb7f5c209913e8229d1f2cf4365))

* chore(ci): fixed semantic-release config ([`18c4da3`](https://github.com/lipov3cz3k/aicooking-ble/commit/18c4da392a0fb5597cc9cc5c852822ab8be43f68))

* chore(deps): bump snok/install-poetry from 1.3.3 to 1.3.4

Bumps [snok/install-poetry](https://github.com/snok/install-poetry) from 1.3.3 to 1.3.4.
- [Release notes](https://github.com/snok/install-poetry/releases)
- [Commits](https://github.com/snok/install-poetry/compare/v1.3.3...v1.3.4)

---
updated-dependencies:
- dependency-name: snok/install-poetry
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ae91904`](https://github.com/lipov3cz3k/aicooking-ble/commit/ae91904f477c657ba1fade4688c13b66ed9eac56))

* chore(deps): bump relekang/python-semantic-release from 7.33.3 to 8.0.4

Bumps [relekang/python-semantic-release](https://github.com/relekang/python-semantic-release) from 7.33.3 to 8.0.4.
- [Release notes](https://github.com/relekang/python-semantic-release/releases)
- [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
- [Commits](https://github.com/relekang/python-semantic-release/compare/v7.33.3...v8.0.4)

---
updated-dependencies:
- dependency-name: relekang/python-semantic-release
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a9baa65`](https://github.com/lipov3cz3k/aicooking-ble/commit/a9baa65427777d1f3c519d90a63540b43e36716b))

* chore(deps): bump wagoid/commitlint-github-action from 5.4.1 to 5.4.3

Bumps [wagoid/commitlint-github-action](https://github.com/wagoid/commitlint-github-action) from 5.4.1 to 5.4.3.
- [Changelog](https://github.com/wagoid/commitlint-github-action/blob/master/CHANGELOG.md)
- [Commits](https://github.com/wagoid/commitlint-github-action/compare/v5.4.1...v5.4.3)

---
updated-dependencies:
- dependency-name: wagoid/commitlint-github-action
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`e6fbd30`](https://github.com/lipov3cz3k/aicooking-ble/commit/e6fbd305767789bef06b215b68b229210daf3378))

* chore(deps-dev): bump sphinx-rtd-theme from 1.2.0 to 1.2.2

Bumps [sphinx-rtd-theme](https://github.com/readthedocs/sphinx_rtd_theme) from 1.2.0 to 1.2.2.
- [Changelog](https://github.com/readthedocs/sphinx_rtd_theme/blob/master/docs/changelog.rst)
- [Commits](https://github.com/readthedocs/sphinx_rtd_theme/compare/1.2.0...1.2.2)

---
updated-dependencies:
- dependency-name: sphinx-rtd-theme
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a159e35`](https://github.com/lipov3cz3k/aicooking-ble/commit/a159e356d5da638cf5ea85264085e21a2dd73d02))

* chore(deps-dev): bump pytest-cov from 4.0.0 to 4.1.0

Bumps [pytest-cov](https://github.com/pytest-dev/pytest-cov) from 4.0.0 to 4.1.0.
- [Changelog](https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest-cov/compare/v4.0.0...v4.1.0)

---
updated-dependencies:
- dependency-name: pytest-cov
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`88f402f`](https://github.com/lipov3cz3k/aicooking-ble/commit/88f402f093b826d44801f09a230430616eb7d82b))

* chore(deps-dev): bump sphinx from 6.1.3 to 6.2.1

Bumps [sphinx](https://github.com/sphinx-doc/sphinx) from 6.1.3 to 6.2.1.
- [Release notes](https://github.com/sphinx-doc/sphinx/releases)
- [Changelog](https://github.com/sphinx-doc/sphinx/blob/master/CHANGES)
- [Commits](https://github.com/sphinx-doc/sphinx/compare/v6.1.3...v6.2.1)

---
updated-dependencies:
- dependency-name: sphinx
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`9309ce4`](https://github.com/lipov3cz3k/aicooking-ble/commit/9309ce4e1b1c474b9736764be1d45d88f52051a0))

* chore(deps): bump relekang/python-semantic-release from 7.33.2 to 7.33.3

Bumps [relekang/python-semantic-release](https://github.com/relekang/python-semantic-release) from 7.33.2 to 7.33.3.
- [Release notes](https://github.com/relekang/python-semantic-release/releases)
- [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
- [Commits](https://github.com/relekang/python-semantic-release/compare/v7.33.2...v7.33.3)

---
updated-dependencies:
- dependency-name: relekang/python-semantic-release
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`145335a`](https://github.com/lipov3cz3k/aicooking-ble/commit/145335a96082139aa9096a0c9784b542fd8aa5b0))

* chore(deps): bump wagoid/commitlint-github-action from 5.3.1 to 5.4.1

Bumps [wagoid/commitlint-github-action](https://github.com/wagoid/commitlint-github-action) from 5.3.1 to 5.4.1.
- [Release notes](https://github.com/wagoid/commitlint-github-action/releases)
- [Changelog](https://github.com/wagoid/commitlint-github-action/blob/master/CHANGELOG.md)
- [Commits](https://github.com/wagoid/commitlint-github-action/compare/v5.3.1...v5.4.1)

---
updated-dependencies:
- dependency-name: wagoid/commitlint-github-action
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`c64fc9f`](https://github.com/lipov3cz3k/aicooking-ble/commit/c64fc9f08a783167563bb6f5c290c492bdd38fc5))

* chore(deps-dev): bump pytest from 7.2.2 to 7.3.1

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.2.2 to 7.3.1.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.2.2...7.3.1)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`068ff40`](https://github.com/lipov3cz3k/aicooking-ble/commit/068ff406695262851174e93bf93a9001974315be))

* chore(deps-dev): bump myst-parser from 0.19.1 to 1.0.0

Bumps [myst-parser](https://github.com/executablebooks/MyST-Parser) from 0.19.1 to 1.0.0.
- [Release notes](https://github.com/executablebooks/MyST-Parser/releases)
- [Changelog](https://github.com/executablebooks/MyST-Parser/blob/master/CHANGELOG.md)
- [Commits](https://github.com/executablebooks/MyST-Parser/compare/v0.19.1...v1.0.0)

---
updated-dependencies:
- dependency-name: myst-parser
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`90aa2e0`](https://github.com/lipov3cz3k/aicooking-ble/commit/90aa2e07edb0c266e775cc40f228b68770db505d))

* chore(deps-dev): bump pytest-cov from 3.0.0 to 4.0.0

Bumps [pytest-cov](https://github.com/pytest-dev/pytest-cov) from 3.0.0 to 4.0.0.
- [Release notes](https://github.com/pytest-dev/pytest-cov/releases)
- [Changelog](https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest-cov/compare/v3.0.0...v4.0.0)

---
updated-dependencies:
- dependency-name: pytest-cov
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`da8eefb`](https://github.com/lipov3cz3k/aicooking-ble/commit/da8eefb809717df9f0cf6e604d375c121fbad4f3))

* chore(deps-dev): bump sphinx from 5.3.0 to 6.1.3

Bumps [sphinx](https://github.com/sphinx-doc/sphinx) from 5.3.0 to 6.1.3.
- [Release notes](https://github.com/sphinx-doc/sphinx/releases)
- [Changelog](https://github.com/sphinx-doc/sphinx/blob/master/CHANGES)
- [Commits](https://github.com/sphinx-doc/sphinx/compare/v5.3.0...v6.1.3)

---
updated-dependencies:
- dependency-name: sphinx
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`d965351`](https://github.com/lipov3cz3k/aicooking-ble/commit/d9653514e6a02c7e3ef0b9d8fd8921fca73f935d))

* chore(deps-dev): bump pytest from 7.2.1 to 7.2.2

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.2.1 to 7.2.2.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.2.1...7.2.2)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a0102e8`](https://github.com/lipov3cz3k/aicooking-ble/commit/a0102e8f00687865b49194caee72715baac71197))

* chore(deps-dev): bump myst-parser from 0.18.1 to 0.19.1

Bumps [myst-parser](https://github.com/executablebooks/MyST-Parser) from 0.18.1 to 0.19.1.
- [Release notes](https://github.com/executablebooks/MyST-Parser/releases)
- [Changelog](https://github.com/executablebooks/MyST-Parser/blob/master/CHANGELOG.md)
- [Commits](https://github.com/executablebooks/MyST-Parser/compare/v0.18.1...v0.19.1)

---
updated-dependencies:
- dependency-name: myst-parser
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`bb84f4e`](https://github.com/lipov3cz3k/aicooking-ble/commit/bb84f4e6ae395b63697fe7196cea8baafd79b8c2))

* chore(deps): bump wagoid/commitlint-github-action from 5.3.0 to 5.3.1

Bumps [wagoid/commitlint-github-action](https://github.com/wagoid/commitlint-github-action) from 5.3.0 to 5.3.1.
- [Release notes](https://github.com/wagoid/commitlint-github-action/releases)
- [Changelog](https://github.com/wagoid/commitlint-github-action/blob/master/CHANGELOG.md)
- [Commits](https://github.com/wagoid/commitlint-github-action/compare/v5.3.0...v5.3.1)

---
updated-dependencies:
- dependency-name: wagoid/commitlint-github-action
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f6d3f99`](https://github.com/lipov3cz3k/aicooking-ble/commit/f6d3f99d0e8c70b72ec5a04bcd92f29f48c0bd6e))

* chore(ci): set up dependabot for Github Actions ([`3131c2c`](https://github.com/lipov3cz3k/aicooking-ble/commit/3131c2c45e767b4e7fec3d3edbdae02248bad4b4))

### Ci

* ci: remove hacktoberfest workflows ([`2a56845`](https://github.com/lipov3cz3k/aicooking-ble/commit/2a56845fedf3135a3cc388a0e2f202efec0875ac))

### Documentation

* docs: update README code style badge to ruff ([`36bf137`](https://github.com/lipov3cz3k/aicooking-ble/commit/36bf137c45f1c5297a23e19b442e4a654e5c7dac))

### Feature

* feat(project): support Python 3.11+ and Ruff formatting ([`3d36f8f`](https://github.com/lipov3cz3k/aicooking-ble/commit/3d36f8f1183d9433e8ccbaad5ad7c7ce6725da90))

### Refactor

* refactor(tests): update import of BluetoothServiceInfo to home_assistant_bluetooth ([`65f9ee9`](https://github.com/lipov3cz3k/aicooking-ble/commit/65f9ee9a9a6bf9e1b8d45ef2e8b727c4222cf606))

### Style

* style: apply ruff formatting and adjust lint rules ([`701cb5a`](https://github.com/lipov3cz3k/aicooking-ble/commit/701cb5a9feb29b458960face5206072f0e10b8b5))

### Test

* test: expand parser coverage to 100% ([`150a4b4`](https://github.com/lipov3cz3k/aicooking-ble/commit/150a4b45271b00949ba1ebdc398cb898b73f6272))

### Unknown

* Merge pull request #105 from lipov3cz3k/pypi-oidc

chore(ci): switch PyPI publishing to Trusted Publisher OIDC ([`95f275f`](https://github.com/lipov3cz3k/aicooking-ble/commit/95f275fc2c3822c87aaae68f6c8e4d1ffec3567a))

* Merge pull request #104 from lipov3cz3k/update-readme

docs: update README code style badge to ruff ([`6881d30`](https://github.com/lipov3cz3k/aicooking-ble/commit/6881d3033c0ce0fd107f65cb201afba94383fdec))

* Merge pull request #103 from lipov3cz3k/expand-tests

test: expand parser coverage to 100% ([`7ffed61`](https://github.com/lipov3cz3k/aicooking-ble/commit/7ffed61a91c7e0423518241b43578346f85aa0fc))

* Merge pull request #102 from lipov3cz3k/modernize-project

chore(project): modernize project setup and update dependencies ([`d974304`](https://github.com/lipov3cz3k/aicooking-ble/commit/d974304277eb466af46f42fdc1d856d10286f720))

* Merge pull request #87 from lipov3cz3k/dependabot/github_actions/wagoid/commitlint-github-action-6.0.1

chore(deps): bump wagoid/commitlint-github-action from 5.4.5 to 6.2.1 ([`c2a1f70`](https://github.com/lipov3cz3k/aicooking-ble/commit/c2a1f703a29f2466e5abb767311b3bf04e6109bd))

* Merge pull request #98 from lipov3cz3k/dependabot/pip/pytest-8.2.2

chore(deps-dev): bump pytest from 8.1.1 to 8.2.2 ([`d99f123`](https://github.com/lipov3cz3k/aicooking-ble/commit/d99f123468a2ea1372289ac6e19e5d9bbdbf0fed))

* Merge pull request #100 from lipov3cz3k/dependabot/github_actions/relekang/python-semantic-release-9.8.3

chore(deps): bump relekang/python-semantic-release from 9.4.0 to 9.8.3 ([`d87d370`](https://github.com/lipov3cz3k/aicooking-ble/commit/d87d370c4f6c68ee96ce6c4444987ff5f86a6831))

* Merge pull request #84 from lipov3cz3k/dependabot/github_actions/relekang/python-semantic-release-9.4.0

chore(deps): bump relekang/python-semantic-release from 9.1.1 to 9.4.0 ([`101becd`](https://github.com/lipov3cz3k/aicooking-ble/commit/101becdd917a636aa41509324dbb2b8611ef9f77))

* Merge pull request #48 from lipov3cz3k/dependabot/pip/bluetooth-sensor-state-data-1.6.2

chore(deps): bump bluetooth-sensor-state-data from 1.6.1 to 1.6.2 ([`bdcbd67`](https://github.com/lipov3cz3k/aicooking-ble/commit/bdcbd6791fd5339d53cd4c6877042f717e28530c))

* Merge pull request #55 from lipov3cz3k/dependabot/pip/sensor-state-data-2.18.0

chore(deps): bump sensor-state-data from 2.17.1 to 2.18.0 ([`3491c5d`](https://github.com/lipov3cz3k/aicooking-ble/commit/3491c5d95403da8c4eb0398e1ab22c8f2d23e8b4))

* Merge pull request #56 from lipov3cz3k/dependabot/pip/home-assistant-bluetooth-1.10.4

chore(deps): bump home-assistant-bluetooth from 1.10.3 to 1.10.4 ([`916dd9a`](https://github.com/lipov3cz3k/aicooking-ble/commit/916dd9ae82ad787f9fdb39cd800de215e7a5c92a))

* Merge pull request #68 from lipov3cz3k/dependabot/github_actions/wagoid/commitlint-github-action-5.4.5

chore(deps): bump wagoid/commitlint-github-action from 5.4.4 to 5.4.5 ([`ccc15d8`](https://github.com/lipov3cz3k/aicooking-ble/commit/ccc15d8ef70294dca77af4680a6959cbb0792919))

* Merge pull request #71 from lipov3cz3k/dependabot/github_actions/codecov/codecov-action-4

chore(deps): bump codecov/codecov-action from 3 to 4 ([`c7152e9`](https://github.com/lipov3cz3k/aicooking-ble/commit/c7152e9d18e7aab8a0c51b494cb8ac4140a59d5d))

* Merge pull request #72 from lipov3cz3k/dependabot/github_actions/tiangolo/issue-manager-0.5.0

chore(deps): bump tiangolo/issue-manager from 0.4.0 to 0.5.0 ([`d9f83b1`](https://github.com/lipov3cz3k/aicooking-ble/commit/d9f83b1c7290ba85a78fbeb7dc64e6f28a3ce47c))

* Merge pull request #73 from lipov3cz3k/dependabot/github_actions/pre-commit/action-3.0.1

chore(deps): bump pre-commit/action from 3.0.0 to 3.0.1 ([`f7952ed`](https://github.com/lipov3cz3k/aicooking-ble/commit/f7952ed3e5609ad290e5ecb4142176b2faa9a8a4))

* Merge pull request #78 from lipov3cz3k/dependabot/github_actions/relekang/python-semantic-release-9.1.1

chore(deps): bump relekang/python-semantic-release from 8.5.1 to 9.1.1 ([`5509883`](https://github.com/lipov3cz3k/aicooking-ble/commit/55098836320e80f5781eef59280468fab8bdc057))

* Merge pull request #80 from lipov3cz3k/dependabot/pip/pytest-8.1.1

chore(deps-dev): bump pytest from 7.4.3 to 8.1.1 ([`1ab6376`](https://github.com/lipov3cz3k/aicooking-ble/commit/1ab6376b3206e3198776b0b65bd7327242b674f1))

* Merge pull request #62 from lipov3cz3k/dependabot/github_actions/actions/setup-python-5

chore(deps): bump actions/setup-python from 4 to 5 ([`5fa3bd2`](https://github.com/lipov3cz3k/aicooking-ble/commit/5fa3bd262c1bf2e484fdeedec0dca5a8e8925767))

* Merge pull request #60 from lipov3cz3k/dependabot/pip/sphinx-rtd-theme-2.0.0

chore(deps-dev): bump sphinx-rtd-theme from 1.3.0 to 2.0.0 ([`faaf879`](https://github.com/lipov3cz3k/aicooking-ble/commit/faaf879c28d5982034c02a4d89f851af0a02f769))

* Merge pull request #63 from lipov3cz3k/dependabot/github_actions/relekang/python-semantic-release-8.5.1

chore(deps): bump relekang/python-semantic-release from 8.1.1 to 8.5.1 ([`c07a6be`](https://github.com/lipov3cz3k/aicooking-ble/commit/c07a6be3c5efc0f5c21db2775785c6fd5289e70d))

* Merge pull request #58 from lipov3cz3k/dependabot/pip/pytest-7.4.3

chore(deps-dev): bump pytest from 7.4.2 to 7.4.3 ([`3a02817`](https://github.com/lipov3cz3k/aicooking-ble/commit/3a0281730265b7d0cce07c39fc5902068c47f920))

* Merge pull request #59 from lipov3cz3k/dependabot/github_actions/wagoid/commitlint-github-action-5.4.4

chore(deps): bump wagoid/commitlint-github-action from 5.4.3 to 5.4.4 ([`10e9508`](https://github.com/lipov3cz3k/aicooking-ble/commit/10e95080a2c1707481a897a674699bcee48630f2))

* Merge pull request #49 from lipov3cz3k/dependabot/pip/sphinx-rtd-theme-1.3.0

chore(deps-dev): bump sphinx-rtd-theme from 1.2.2 to 1.3.0 ([`bda432f`](https://github.com/lipov3cz3k/aicooking-ble/commit/bda432f8c53ca1da44dbfa0d90316bf6d5bebc21))

* Merge pull request #51 from lipov3cz3k/dependabot/pip/myst-parser-2.0.0

chore(deps-dev): bump myst-parser from 1.0.0 to 2.0.0 ([`2807008`](https://github.com/lipov3cz3k/aicooking-ble/commit/28070081392f144ec6c201547f55e969753030af))

* Merge pull request #50 from lipov3cz3k/dependabot/pip/sphinx-7.2.6

chore(deps-dev): bump sphinx from 6.2.1 to 7.2.6 ([`eb3e37e`](https://github.com/lipov3cz3k/aicooking-ble/commit/eb3e37ef27a86b38365573eef33843b05b9c858d))

* Merge pull request #53 from lipov3cz3k/dependabot/github_actions/relekang/python-semantic-release-8.1.1

chore(deps): bump relekang/python-semantic-release from 8.0.4 to 8.1.1 ([`fce57b7`](https://github.com/lipov3cz3k/aicooking-ble/commit/fce57b7e3f30deef1efb97996dfdc2cfa77b4f87))

* Merge pull request #52 from lipov3cz3k/dependabot/github_actions/actions/checkout-4

chore(deps): bump actions/checkout from 3 to 4 ([`90d3e66`](https://github.com/lipov3cz3k/aicooking-ble/commit/90d3e668cc9f5c252d0a834b610b10ea1cfa0dd9))

* Merge pull request #47 from lipov3cz3k/dependabot/pip/home-assistant-bluetooth-1.10.3

chore(deps): bump home-assistant-bluetooth from 1.9.3 to 1.10.3 ([`05272f0`](https://github.com/lipov3cz3k/aicooking-ble/commit/05272f009d5f12e8c00cff9646d72f3681620dae))

* Merge pull request #41 from lipov3cz3k/dependabot/pip/sensor-state-data-2.17.1

chore(deps): bump sensor-state-data from 2.13.0 to 2.17.1 ([`ab57a20`](https://github.com/lipov3cz3k/aicooking-ble/commit/ab57a20bd405ca8338edaa4624bfe2f969f15fcc))

* Merge pull request #46 from lipov3cz3k/dependabot/pip/pytest-7.4.2

chore(deps-dev): bump pytest from 7.3.1 to 7.4.2 ([`2cc93df`](https://github.com/lipov3cz3k/aicooking-ble/commit/2cc93df556a532e62fe929b9235ad8e4c5ff9a17))

* Merge pull request #39 from lipov3cz3k/dependabot/github_actions/wagoid/commitlint-github-action-5.4.3

chore(deps): bump wagoid/commitlint-github-action from 5.4.1 to 5.4.3 ([`026abe7`](https://github.com/lipov3cz3k/aicooking-ble/commit/026abe7c797ba69a29551c6135f1c48cd0c4e937))

* Merge pull request #32 from lipov3cz3k/dependabot/pip/sphinx-rtd-theme-1.2.2

chore(deps-dev): bump sphinx-rtd-theme from 1.2.0 to 1.2.2 ([`3cf902a`](https://github.com/lipov3cz3k/aicooking-ble/commit/3cf902a4caf687aa08d8a8183a183215b5147f70))

* Merge pull request #45 from lipov3cz3k/chore-semantic-release

chore(ci): fixed semantic-release config ([`287c7a7`](https://github.com/lipov3cz3k/aicooking-ble/commit/287c7a78cac9e2eeb1375546a188bbb631f8b83e))

* Merge pull request #28 from lipov3cz3k/dependabot/pip/pytest-cov-4.1.0

chore(deps-dev): bump pytest-cov from 4.0.0 to 4.1.0 ([`b912e66`](https://github.com/lipov3cz3k/aicooking-ble/commit/b912e66be30c4c729f5be88db762a6f77266a63f))

* Merge pull request #42 from lipov3cz3k/dependabot/github_actions/relekang/python-semantic-release-8.0.4

chore(deps): bump relekang/python-semantic-release from 7.33.3 to 8.0.4 ([`c6236e1`](https://github.com/lipov3cz3k/aicooking-ble/commit/c6236e152e17d46fcafed54c8bcfd87de8258927))

* Merge pull request #44 from lipov3cz3k/dependabot/github_actions/snok/install-poetry-1.3.4

chore(deps): bump snok/install-poetry from 1.3.3 to 1.3.4 ([`d3125a6`](https://github.com/lipov3cz3k/aicooking-ble/commit/d3125a6884597e2b2118004c3782e1674b533ed1))

* Merge pull request #20 from lipov3cz3k/dependabot/github_actions/wagoid/commitlint-github-action-5.4.1

chore(deps): bump wagoid/commitlint-github-action from 5.3.1 to 5.4.1 ([`71c2b19`](https://github.com/lipov3cz3k/aicooking-ble/commit/71c2b1987b426b15390b294e234145976039c1e8))

* Merge pull request #23 from lipov3cz3k/dependabot/pip/sphinx-6.2.1

chore(deps-dev): bump sphinx from 6.1.3 to 6.2.1 ([`6060541`](https://github.com/lipov3cz3k/aicooking-ble/commit/6060541e9bf5aa6b448493223b34995074faac13))

* Merge pull request #22 from lipov3cz3k/dependabot/github_actions/relekang/python-semantic-release-7.33.3

chore(deps): bump relekang/python-semantic-release from 7.33.2 to 7.33.3 ([`80d67f8`](https://github.com/lipov3cz3k/aicooking-ble/commit/80d67f86b14501cc90073f1ad3b54cb414708f25))

* Merge pull request #19 from lipov3cz3k/dependabot/pip/pytest-7.3.1

chore(deps-dev): bump pytest from 7.2.2 to 7.3.1 ([`dd789ee`](https://github.com/lipov3cz3k/aicooking-ble/commit/dd789ee4c3a50fa815a1d0bab8d609e4bc02c5a9))

* Merge pull request #17 from lipov3cz3k/dependabot/pip/myst-parser-1.0.0

chore(deps-dev): bump myst-parser from 0.19.1 to 1.0.0 ([`d6c7aae`](https://github.com/lipov3cz3k/aicooking-ble/commit/d6c7aae80521f435282020e91ce4b11397bd8355))

* Merge pull request #12 from lipov3cz3k/dependabot/pip/myst-parser-0.19.1

chore(deps-dev): bump myst-parser from 0.18.1 to 0.19.1 ([`2716ac7`](https://github.com/lipov3cz3k/aicooking-ble/commit/2716ac7cb159e13163e4affea8a190de89fb5b8c))

* Merge pull request #15 from lipov3cz3k/dependabot/pip/pytest-cov-4.0.0

chore(deps-dev): bump pytest-cov from 3.0.0 to 4.0.0 ([`267528b`](https://github.com/lipov3cz3k/aicooking-ble/commit/267528b67a0e2db3dbe486b202f3d02af0cdddae))

* Merge pull request #14 from lipov3cz3k/dependabot/pip/sphinx-6.1.3

chore(deps-dev): bump sphinx from 5.3.0 to 6.1.3 ([`4296bf9`](https://github.com/lipov3cz3k/aicooking-ble/commit/4296bf943845ec06bfb2c59190b092da09092292))

* Merge pull request #13 from lipov3cz3k/dependabot/pip/pytest-7.2.2

chore(deps-dev): bump pytest from 7.2.1 to 7.2.2 ([`df8ce73`](https://github.com/lipov3cz3k/aicooking-ble/commit/df8ce73eb3ac2b83c6c8e6dfba673fcb3f2db941))

* Merge pull request #11 from lipov3cz3k/dependabot/github_actions/wagoid/commitlint-github-action-5.3.1

chore(deps): bump wagoid/commitlint-github-action from 5.3.0 to 5.3.1 ([`31e2101`](https://github.com/lipov3cz3k/aicooking-ble/commit/31e21015612298fba97c4295f99922ca71187f7e))

## v0.1.2 (2023-02-20)

### Chore

* chore(deps): poetry update ([`f704987`](https://github.com/lipov3cz3k/aicooking-ble/commit/f704987f10d3e312f0a7e36bd98b6c79af56cea6))

* chore(deps): switch from caret to inequality version constraints ([`9fa028b`](https://github.com/lipov3cz3k/aicooking-ble/commit/9fa028b0bb7657fdad62844cb3cc52fc4bacdff0))

* chore(deps-dev): bump pre-commit hooks ([`916da7e`](https://github.com/lipov3cz3k/aicooking-ble/commit/916da7e8b45b11d33a496897961bbf5f603bb14c))

* chore(deps): bump home-assistant-bluetooth from 1.9.2 to 1.9.3

Bumps [home-assistant-bluetooth](https://github.com/home-assistant-libs/home-assistant-bluetooth) from 1.9.2 to 1.9.3.
- [Release notes](https://github.com/home-assistant-libs/home-assistant-bluetooth/releases)
- [Changelog](https://github.com/home-assistant-libs/home-assistant-bluetooth/blob/main/CHANGELOG.md)
- [Commits](https://github.com/home-assistant-libs/home-assistant-bluetooth/compare/v1.9.2...v1.9.3)

---
updated-dependencies:
- dependency-name: home-assistant-bluetooth
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f36292b`](https://github.com/lipov3cz3k/aicooking-ble/commit/f36292bea19831a2e977bbef7546629668193e64))

* chore(deps-dev): bump sphinx-rtd-theme from 1.1.1 to 1.2.0

Bumps [sphinx-rtd-theme](https://github.com/readthedocs/sphinx_rtd_theme) from 1.1.1 to 1.2.0.
- [Release notes](https://github.com/readthedocs/sphinx_rtd_theme/releases)
- [Changelog](https://github.com/readthedocs/sphinx_rtd_theme/blob/master/docs/changelog.rst)
- [Commits](https://github.com/readthedocs/sphinx_rtd_theme/compare/1.1.1...1.2.0)

---
updated-dependencies:
- dependency-name: sphinx-rtd-theme
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`9db3ea5`](https://github.com/lipov3cz3k/aicooking-ble/commit/9db3ea5b08cc9cbceeaa7242cb638f636ebed906))

* chore(deps-dev): bump pytest from 7.2.0 to 7.2.1

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.2.0 to 7.2.1.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.2.0...7.2.1)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7017451`](https://github.com/lipov3cz3k/aicooking-ble/commit/70174515da016fe88e3ecbe917d80d3fadfb4313))

* chore: add dependabot config ([`4ebd993`](https://github.com/lipov3cz3k/aicooking-ble/commit/4ebd99372850bcf36f659f49b54e8829a4ce97a6))

### Fix

* fix: update python semantic release job ([`540f8b2`](https://github.com/lipov3cz3k/aicooking-ble/commit/540f8b25de819e1a26570d29b55df870fe465b21))

* fix: account for switching adapter when finding changed_manufacturer_data ([`d3aebaf`](https://github.com/lipov3cz3k/aicooking-ble/commit/d3aebaf72540b28ab24ccdc1f603f37f7e31f4b6))

### Unknown

* Merge pull request #10 from lipov3cz3k/actions

fix: update python semantic release job ([`a0a5c8e`](https://github.com/lipov3cz3k/aicooking-ble/commit/a0a5c8ea95a87da1d798c50cfe325f4e10d5c85a))

* Merge pull request #9 from lipov3cz3k/dependencies

Update dependencies ([`0ea53d4`](https://github.com/lipov3cz3k/aicooking-ble/commit/0ea53d4fe12247450cf75a6904f969849a427194))

* Merge pull request #6 from lipov3cz3k/dependabot/pip/sphinx-rtd-theme-1.2.0

chore(deps-dev): bump sphinx-rtd-theme from 1.1.1 to 1.2.0 ([`32b6c9f`](https://github.com/lipov3cz3k/aicooking-ble/commit/32b6c9f2c2121ec22e33ca76cef06715540d3bd3))

* Merge pull request #8 from lipov3cz3k/dependabot/pip/home-assistant-bluetooth-1.9.3

chore(deps): bump home-assistant-bluetooth from 1.9.2 to 1.9.3 ([`cdb8c33`](https://github.com/lipov3cz3k/aicooking-ble/commit/cdb8c334a7ae2e4a45d9db71488214bfa0047bd1))

* Merge pull request #5 from lipov3cz3k/dependabot/pip/pytest-7.2.1

chore(deps-dev): bump pytest from 7.2.0 to 7.2.1 ([`8ea6fe5`](https://github.com/lipov3cz3k/aicooking-ble/commit/8ea6fe5f74566b12911d1a1ba2ae5486200ecd23))

## v0.1.1 (2023-01-05)

### Fix

* fix: bump dependencies ([`f1d1e46`](https://github.com/lipov3cz3k/aicooking-ble/commit/f1d1e46d12d88aa0d362575da49d7bfe2e6ff5db))

### Unknown

* Merge pull request #4 from lipov3cz3k/update

fix: bump dependencies ([`633bff1`](https://github.com/lipov3cz3k/aicooking-ble/commit/633bff1820c089a717e95d54890941dfb3d6da6b))

## v0.1.0 (2023-01-04)

### Feature

* feat: init Aicooking parser ([`aa31512`](https://github.com/lipov3cz3k/aicooking-ble/commit/aa31512141ed7dc27267343c7a3580ab42230da8))

### Fix

* fix: downgrade home-assistant-bluetooth, due to missing bleak dependency ([`4c6941c`](https://github.com/lipov3cz3k/aicooking-ble/commit/4c6941cbc2c271213d6351756e6283fb454ac2e1))

### Unknown

* Merge pull request #3 from lipov3cz3k/aicooker

Aicooking parser ([`d917c01`](https://github.com/lipov3cz3k/aicooking-ble/commit/d917c0122c57c2e021d6545d9e5c82495bfd650c))

## v0.0.1 (2023-01-03)

### Chore

* chore: initial commit ([`a680253`](https://github.com/lipov3cz3k/aicooking-ble/commit/a680253d1b0dca7afc1d1df0eeb95987d8ea0b3f))

### Fix

* fix: bump python min to 3.9

see https://github.com/Bluetooth-Devices/govee-ble/pull/3 ([`c901215`](https://github.com/lipov3cz3k/aicooking-ble/commit/c901215995976c92f5a2a343d70bc82d1d59a8f6))

### Unknown

* Merge pull request #2 from lipov3cz3k/bump_python

fix: bump python min to 3.9 ([`1e49782`](https://github.com/lipov3cz3k/aicooking-ble/commit/1e4978207b869eee483de5ef669a8399c50aa33a))
