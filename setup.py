from setuptools import setup, find_packages

setup(
    name="files-kedro",
    version="0.1",
    description="Meltano project files for kedro",
    packages=find_packages(),
    package_data={
        "bundle": [
            "utilities/kedro/README.md",
            "utilities/kedro/run.py",
            "utilities/kedro/setup.cfg",
            "utilities/kedro/pyproject.toml",
            "utilities/kedro/.gitignore",
            "utilities/kedro/__init__.py",
            "utilities/kedro/conf/**",
            "utilities/kedro/conf/base/*.yml",
            "utilities/kedro/conf/local/*.yml",
            "utilities/kedro/data/01_raw/iris.csv",          
            "utilities/kedro/data/**/.gitkeep",                      
            "utilities/kedro/docs/source/conf.py",          
            "utilities/kedro/docs/source/index.rst",                      
            "utilities/kedro/logs/.gitkeep",          
            "utilities/kedro/notebooks/.gitkeep",          
            "utilities/kedro/src/requirements.txt",
            "utilities/kedro/src/*.py",
            "utilities/kedro/src/tests/*.py",
            "utilities/kedro/src/meltano_kedro/*.py",            
        ]
    },
)
