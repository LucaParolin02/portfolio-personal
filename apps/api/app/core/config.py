from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Configuración central de la API.

    En local se lee desde apps/api/.env.
    En producción se puede inyectar desde Docker Compose o variables del servidor.
    """

    APP_NAME: str = "Portfolio Personal API"
    ENVIRONMENT: str = "local"

    API_V1_PREFIX: str = "/api/v1"

    DATABASE_URL: str

    FRONTEND_ORIGINS: str = "http://localhost:5173"

    CONTACT_TARGET_EMAIL: str

    SMTP_HOST: str
    SMTP_PORT: int = 587
    SMTP_USERNAME: str
    SMTP_PASSWORD: str
    SMTP_FROM_EMAIL: str
    SMTP_FROM_NAME: str = "Portfolio Contact"

    @property
    def cors_origins(self) -> list[str]:
        """
        Convierte:
        FRONTEND_ORIGINS=http://localhost:5173,http://localhost:4173

        en:
        ["http://localhost:5173", "http://localhost:4173"]
        """

        return [
            origin.strip()
            for origin in self.FRONTEND_ORIGINS.split(",")
            if origin.strip()
        ]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()