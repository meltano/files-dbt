from setuptools import setup, find_packages

setup(
    name="files-dbt-snowflake",
    version="0.4",
    description="Meltano project files for dbt on Snowflake",
    packages=find_packages(),
    package_data={
        "bundle": [
            "transform/profile/snowflake-profiles.yml",
        ]
    },
)
