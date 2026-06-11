from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Configuración central de la API.

    En local, estos valores se leen desde apps/api/.env.
    En producción, se inyectarán como variables de entorno desde Docker Compose
    o desde el servidor.
    """

    APP_NAME: str = "Portfolio Personal API"
    ENVIRONMENT: str = "local"

    FRONTEND_ORIGIN: str = "http://localhost:5173"

    API_V1_PREFIX: str = "/api/v1"

    DATABASE_URL: str

    CONTACT_TARGET_EMAIL: str

    SMTP_HOST: str
    SMTP_PORT: int = 587
    SMTP_USERNAME: str
    SMTP_PASSWORD: str
    SMTP_FROM_EMAIL: str
    SMTP_FROM_NAME: str = "Portfolio Contact"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()