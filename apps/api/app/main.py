from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers import experience, health, profile, projects, skills
from app.core.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    version="0.2.0",
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

app.include_router(
    profile.router,
    prefix=settings.API_V1_PREFIX,
    tags=["profile"],
)

app.include_router(
    projects.router,
    prefix=settings.API_V1_PREFIX,
    tags=["projects"],
)

app.include_router(
    skills.router,
    prefix=settings.API_V1_PREFIX,
    tags=["skills"],
)

app.include_router(
    experience.router,
    prefix=settings.API_V1_PREFIX,
    tags=["experience"],
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Portfolio Personal API running",
        "environment": settings.ENVIRONMENT,
    }