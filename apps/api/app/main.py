from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers import health
from app.core.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    description="API personal para portfolio, proyectos, experiencia, skills y contacto.",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    health.router,
    prefix=settings.API_V1_PREFIX,
    tags=["health"],
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Portfolio Personal API running",
        "environment": settings.ENVIRONMENT,
    }