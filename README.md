# files-kedro

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) for [Kedro](https://kedro.readthedocs.io/en/stable/)

This plugin will add the following files to your Meltano project:

- `utilities/kedro/setup.cfg`
- `utilities/kedro/pyproject.yml`
- `utilities/kedro/`
- `utilities/kedro/`

## Installation

To install the Kedro file bundle into your Meltano project you need to use a custom file bundle.

```
# Add Kedro files to your Meltano project
meltano add --custom files kedro
```
