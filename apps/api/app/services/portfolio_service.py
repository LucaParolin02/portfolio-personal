from sqlalchemy.orm import Session

from app.repositories import portfolio_db_repository


class PortfolioService:
    """
    Servicio de dominio del portfolio.

    Ahora lee desde PostgreSQL mediante SQLAlchemy.
    Los routers no conocen los detalles de consulta ni de transformación.
    """

    @staticmethod
    def get_profile(db: Session) -> dict | None:
        return portfolio_db_repository.get_profile(db)

    @staticmethod
    def get_projects(db: Session) -> list[dict]:
        return portfolio_db_repository.get_projects(db)

    @staticmethod
    def get_project_by_slug(db: Session, slug: str) -> dict | None:
        return portfolio_db_repository.get_project_by_slug(db, slug)

    @staticmethod
    def get_skills(db: Session) -> list[dict]:
        return portfolio_db_repository.get_skills(db)

    @staticmethod
    def get_experience(db: Session) -> list[dict]:
        return portfolio_db_repository.get_experience(db)