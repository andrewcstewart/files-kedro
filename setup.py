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
            "utilities/kedro/pyproject.yml",
            "utilities/kedro/.gitignore",
            "utilities/kedro/__init__.py",
            "utilities/kedro/conf/*",
            "utilities/kedro/data/*",          
            "utilities/kedro/docs/*",          
            "utilities/kedro/logs/*",          
            "utilities/kedro/notebooks/*",          
            "utilities/kedro/src/*",
        ]
    },
)
