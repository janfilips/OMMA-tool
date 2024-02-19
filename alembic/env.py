from logging.config import fileConfig

from sqlalchemy import create_engine, engine_from_config, pool

from alembic import context
from backend.config import (POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD,
                            POSTGRES_PORT, POSTGRES_USER)
from backend.db.base_class import Base
from backend.db.models import *

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

def reflect_db_schema():
    engine = create_engine(config.get_main_option("sqlalchemy.url"))
    Base.metadata.reflect(bind=engine)

# reflect_db_schema()

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    configuration = config.get_section(config.config_ini_section, {})
    configuration["sqlalchemy.url"] = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

print("Tables in metadata:", ", ".join(sorted(Base.metadata.tables)))
