from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os


POSTGRES_USER = os.getenv("DB_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "flaskdb")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("BD_NAME", "flaskdb")

PG_DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


engine = create_engine(PG_DSN)
env_url = os.getenv("SQLALCHEMY_DATABASE_URI")
if env_url:
    engine = create_engine(env_url)
Session = sessionmaker(engine)