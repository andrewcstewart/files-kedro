# files-kedro

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) for [Kedro](https://kedro.readthedocs.io/en/stable/)

This plugin will add the following files to your Meltano project:

- `utilities/kedro/setup.cfg`
- `utilities/kedro/pyproject.yml`
- `utilities/kedro/run.py`
- `utilities/kedro/README.md`
- `utilities/kedro/.gitignore`
- `utilities/kedro/conf/*`
- `utilities/kedro/src/*`

## Installation

To install the Kedro file bundle into your Meltano project you need to use a custom file bundle.  You will need to provide git+https://github.com/andrewcstewart/files-kedro.git for the `pip_url`.

```
# Add Kedro files to your Meltano project
meltano add --custom files kedro

# Add Kedro as a utility plugin for CLI access
meltano add --custom utility kedro
```

## Configuration

In order to run kedro with meltano you will need to manually add the configuration for the custom utility to `meltano.yml`.

```
plugins:
  utilities:
    - name: kedro
      namespace: kedro
      pip_url: kedro
      executable: kedro
      commands:
        install:
          args: install utilities/kedro/src/
          executable: pip        
        run: 
          args: utilities/kedro/run.py
          executable: python
      settings:
      - name: env
        value: local
        description: Selects which kedro configuration to use (default: local)
        documentation: https://kedro.readthedocs.io/en/stable/kedro_project_setup/configuration.html#additional-configuration-environments
      - name: project_root
        description: The kedro project root path relative to the meltano project root path.
        value: utilities/kedro
      - name: db_username
        description: Database username
      - name: db_password
        description: Database password
        kind: password
      - name: db_host
        description: Database host
      - name: db_port
        description: Database port
      - name: db_database
        description: Database name
      - name: source_table 
        description: Selects which table is used for pipeline input  
      - name: source_schema
        description: Selects which schema is used for pipeline input      
      - name: target_table 
        description: Selects which table is used for pipeline output      
      - name: target_schema
        description: Selects which schema is used for pipeline output
      - name: target_column
        description: Selects which column in the source table is the target variable        
      config:
        env: local
        project_root: utilities/kedro
        db_username: postgres
        db_password: ***
        db_host: localhost
        db_database: postgres
        source_table: input
        source_schema: public
        target_table: output
        target_schema: public
 ```

By default the plugin installs a modified version of the `pandas-iris` starter project which does the following:

1. Inputs a database table 
2. Performs k-NN classifcation on a test set
3. Writes the test set with predictions back to a database table

This is a relatively simple starting point from which you can further develop a ML pipeline for your own needs.

## Usage

Before you can run your kedro pipeline you will need to install its dependencies in the plugins virtual environment.  (Note: this will also install the kedro projet itself as a package; you will want to re-run this any time you make changes to the kedro project.)

```
meltano invoke kedro:install
```

Then to incorporate the kedro pipeline as part of a meltano run-block you can include it in a `meltano run` command like so:

```
meltano run tap-something target-somewhere dbt:run kedro:run
```

