import logging
import time

from backend import config
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger(__name__)


def connect_to_database(retries=5, base_wait_time=2):
    for attempt in range(1, retries + 1):
        try:
            engine = create_engine(config.POSTGRES_URL)
            engine.connect()
            return engine
        except OperationalError as error:
            wait_time = base_wait_time * attempt
            logging.warning(f"Attempt {attempt} of {retries} failed. Retrying in {wait_time} seconds.")
            if attempt < retries:
                time.sleep(wait_time)
            else:
                raise error


engine = connect_to_database()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Create tables in the metadata
Base.metadata.create_all(bind=engine)
