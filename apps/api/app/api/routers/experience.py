from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.experience import ExperienceResponse
from app.services.portfolio_service import PortfolioService

router = APIRouter()


@router.get("/experience", response_model=list[ExperienceResponse])
def get_experience(db: Session = Depends(get_db)) -> list[dict]:
    return PortfolioService.get_experience(db)