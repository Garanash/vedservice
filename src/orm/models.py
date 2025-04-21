import enum
from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated

from database import Base, str_256


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[
    datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow())]

class ArticlesOrm(Base):
    __tablename__ = 'articles'
    id: Mapped[intpk]
    title: Mapped[str_256]

class CompanySellers(Base):
    __tablename__ = 'sellers'


