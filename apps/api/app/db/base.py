from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Clase base para todos los modelos SQLAlchemy.

    Alembic usa esta metadata para detectar las tablas, columnas,
    relaciones y constraints al generar migraciones.
    """

    pass