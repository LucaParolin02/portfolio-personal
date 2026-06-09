from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.project import ProjectResponse
from app.services.portfolio_service import PortfolioService

router = APIRouter()


@router.get("/projects", response_model=list[ProjectResponse])
def get_projects(db: Session = Depends(get_db)) -> list[dict]:
    return PortfolioService.get_projects(db)


@router.get("/projects/{slug}", response_model=ProjectResponse)
def get_project_by_slug(
    slug: str,
    db: Session = Depends(get_db),
) -> dict:
    project = PortfolioService.get_project_by_slug(db, slug)

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with slug '{slug}' was not found.",
        )

    return project