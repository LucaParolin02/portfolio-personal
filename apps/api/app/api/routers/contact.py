from fastapi import APIRouter, HTTPException, Request, status

from app.schemas.contact import ContactMessageRequest, ContactMessageResponse
from app.services.contact_guard_service import ContactGuardService
from app.services.email_service import EmailService


router = APIRouter()


def get_client_ip(request: Request) -> str:
    """
    Obtiene la IP del cliente.

    En producción detrás de NGINX puede llegar por X-Forwarded-For.
    """

    forwarded_for = request.headers.get("x-forwarded-for")

    if forwarded_for:
        return forwarded_for.split(",")[0].strip()

    if request.client is None:
        return "unknown"

    return request.client.host


@router.post("/contact", response_model=ContactMessageResponse)
def send_contact_message(
    payload: ContactMessageRequest,
    request: Request,
) -> ContactMessageResponse:
    client_ip = get_client_ip(request)

    if not ContactGuardService.is_allowed_ip(client_ip):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many contact attempts. Please try again later.",
        )

    if not ContactGuardService.validate_honeypot(payload.company_website):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid contact request.",
        )

    if not ContactGuardService.validate_elapsed_time(payload.form_started_at):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The form was submitted too quickly.",
        )

    try:
        EmailService.send_contact_email(
            sender_name=payload.name.strip(),
            sender_email=str(payload.email),
            message=payload.message.strip(),
        )
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The contact email could not be sent.",
        ) from exc

    return ContactMessageResponse(
        status="ok",
        message="Contact message sent successfully.",
    )