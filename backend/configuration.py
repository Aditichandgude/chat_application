from pydantic_settings import BaseSettings
import databases

class Settings(BaseSettings):
    MYSQL_DATABASE_CONNECTION_STRING: str
    PUBLIC_KEY_FOR_JWT: str

    class Config:
        env_file='backend/.env'
        env_file_encoding='utf-8'

setting=Settings()
database=databases.Database(setting.MYSQL_DATABASE_CONNECTION_STRING)