from typing import Callable, Generator, Type

from fastapi import Depends
from sqlalchemy.orm.session import sessionmaker

from app.repositories.base import BaseRepository
from app.db.session import async_session


def get_session() -> Generator:
    yield async_session


def get_repository(Repo_type: Type[BaseRepository]) -> Callable:
    def get_repo(db: sessionmaker = Depends(get_session)) -> Type[BaseRepository]:
        return Repo_type(db)

    return get_repo
