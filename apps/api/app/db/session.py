from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings


engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
)


SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


def get_db() -> Generator[Session, None, None]:
    """
    Dependencia de FastAPI para obtener una sesión de base de datos.

    Abre una sesión por request y la cierra al finalizar.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()