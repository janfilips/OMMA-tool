import os

CODE_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(CODE_DIR)
DATA_DIR = os.path.join(ROOT_DIR, 'data')

DEVELOPMENT = os.getenv("DEVELOPMENT", None)
STAGING = os.getenv("STAGING", None)
PRODUCTION = os.getenv("PRODUCTION", None)

SECRET_KEY = os.getenv("SECRET_KEY", "h21k3jhk12h3k1hk23hkjqhkdhaskhdksahdiuyi2y7fydweifusehfksdhfkjh")

origins_str = os.getenv("CORS_ORIGINS", "")
if origins_str:
    CORS_ORIGINS = origins_str.split(",")
else:
    CORS_ORIGINS = []

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "omma_devel")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
