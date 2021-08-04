from sqlalchemy.orm import sessionmaker


class BaseRepository:
    def __init__(self, session: sessionmaker) -> None:
        self.session = session
