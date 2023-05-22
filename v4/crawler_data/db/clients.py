# from env_setting_pk.config import (
#     MYSQL_DATA_USER,
#     MYSQL_DATA_PASSWORD,
#     MYSQL_DATA_HOST,
#     MYSQL_DATA_PORT,
#     MYSQL_DATA_DATABASE,
# )

import db.EnvSettingPk.config as EnvConfig

from sqlalchemy import (
    create_engine,
    engine,
)


def get_mysql_financialdata_conn() -> engine.base.Connection:
    address = (
        f"mysql+pymysql://{EnvConfig.MYSQL_DATA_USER}:{EnvConfig.MYSQL_DATA_PASSWORD}@{EnvConfig.MYSQL_DATA_HOST}:{EnvConfig.MYSQL_DATA_PORT}/{EnvConfig.MYSQL_DATA_DATABASE}"
    )
    engine = create_engine(address)
    connect = engine.connect()
    return connect
