import databases
from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

PROJECT_NAME = "PythonTemplate"
VERSION = "1.0.0"
API_PREFIX = "/api"
ALLOWED_HOST_ORIGINS = None

SECRET_KEY = config("SECRET_KEY", cast=Secret, default="CHANGEME")

# PROD
# POSTGRES_USER = config("POSTGRES_USER", cast=str, default="")
# POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret, default="")
# POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="")

# DEV
# POSTGRES_USER = config("POSTGRES_USER", cast=str, default="")
# POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret, default="")
# POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="")

# SIT
# POSTGRES_USER = config("POSTGRES_USER", cast=str, default="")
# POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret, default="")
# POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="")

# LOCAL
POSTGRES_USER = config("POSTGRES_USER", cast=str, default="janus_user")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret, default="j@Nu5.6@t3_p@55.2O22@")
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="34.87.184.130")

POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str, default="mfs")

DATABASE_URL = config(
    "DATABASE_URL",
    cast=DatabaseURL,
    default=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}",
)
print(DATABASE_URL)

database = databases.Database(DATABASE_URL)
