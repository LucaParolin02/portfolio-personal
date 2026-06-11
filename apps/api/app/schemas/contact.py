from pydantic import BaseModel, EmailStr, Field


class ContactMessageRequest(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    message: str = Field(min_length=10, max_length=2000)

    # Honeypot. Debe venir vacío.
    company_website: str | None = Field(default=None, max_length=200)

    # Timestamp generado cuando el usuario carga el formulario.
    form_started_at: int


class ContactMessageResponse(BaseModel):
    status: str
    message: str