# files-dbt

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) for [dbt](https://www.getdbt.com/) using the `Snowflake` adapter.

Files:
- [`transform/models`](./bundle/transform/models) (directory)
- [`transform/profile/snowflake-profiles.yml`](./bundle/transform/profile/snowflake-profiles.yml) `<--` Snowflake-specific profile 
- [`transform/dbt_project.yml`](./bundle/transform/dbt_project.yml)
- [`transform/.gitignore`](./bundle/transform/.gitignore)

```py
# Add dbt transformer and this file bundle to your Meltano project:
meltano add transformer dbt[snowflake]
# Or:
meltano add transformer dbt-snowflake

# Or, add only this file bundle to your Meltano project:
meltano add files dbt-snowflake
```
