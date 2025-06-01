from sqlmodel import SQLModel, create_engine, Session

engine = create_engine("sqlite:///database.db", echo=False)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    return Session(engine)
