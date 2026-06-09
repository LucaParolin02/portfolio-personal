from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.profile import ProfileResponse
from app.services.portfolio_service import PortfolioService


router = APIRouter()


@router.get("/profile", response_model=ProfileResponse)
def get_profile(db: Session = Depends(get_db)) -> dict:
    profile = PortfolioService.get_profile(db)

    if profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile data was not found.",
        )

    return profile