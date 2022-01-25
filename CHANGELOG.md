# Changelog

## 0.4

- Add support for `snowflake` profile as extra: `pip install 'git+https://gitlab.com/meltano/files-dbt.git@config-version-2#egg=repo[snowflake]'`.

## 0.3

- [#3](https://gitlab.com/meltano/files-dbt/-/issues/3) Cast `PG_PORT` to `int` for postgres output in `transform/profile/profiles.yml`

## 0.2

- [#2](https://gitlab.com/meltano/files-dbt/-/issues/2) Add default `bigquery` output to `transform/profile/profiles.yml`

## 0.1

Initial release
