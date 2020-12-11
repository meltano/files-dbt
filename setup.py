from setuptools import setup, find_packages

setup(
    name="files-dbt",
    version="0.2",
    description="Meltano project files for dbt",
    packages=find_packages(),
    package_data={
        "bundle": [
            "transform/models/.gitkeep",
            "transform/profile/profiles.yml",
            "transform/.gitignore",
            "transform/dbt_project.yml",
        ]
    },
)
