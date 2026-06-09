from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.skill import SkillCategoryResponse
from app.services.portfolio_service import PortfolioService

router = APIRouter()


@router.get("/skills", response_model=list[SkillCategoryResponse])
def get_skills(db: Session = Depends(get_db)) -> list[dict]:
    return PortfolioService.get_skills(db)