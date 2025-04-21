from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String
from typing import Annotated

from config import setting

async_engine = create_async_engine(
    url=setting.DATABASE_URL_asyncpg,
    echo=True,
    pool_size=50,
    max_overflow=10,
)
async_session_factory = async_sessionmaker(async_engine)

str_256 = Annotated[str, 256]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }
