from backend.configuration import database, setting
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

engine=create_async_engine(setting.MYSQL_DATABASE_CONNECTION_STRING, echo=True, future=True)

async_session=async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False
)