from fastapi import APIRouter, HTTPException, Request, status

from app.schemas.contact import ContactMessageRequest, ContactMessageResponse
from app.services.contact_guard_service import ContactGuardService
from app.services.email_service import EmailService
from app.services.email_validation_service import EmailValidationService


router = APIRouter()


def get_client_ip(request: Request) -> str:
    """
    Obtiene la IP real del cliente.

    En local usa request.client.host.
    En producción, si la API está detrás de NGINX, intenta usar X-Forwarded-For.
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
            detail="Demasiados intentos de contacto. Probá nuevamente más tarde.",
        )

    if not ContactGuardService.validate_honeypot(payload.company_website):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solicitud de contacto inválida.",
        )

    if not ContactGuardService.validate_elapsed_time(payload.form_started_at):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El formulario fue enviado demasiado rápido.",
        )

    is_valid_email_domain, email_error = EmailValidationService.validate_email_domain(
        str(payload.email)
    )

    if not is_valid_email_domain:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=email_error or "El email ingresado no es válido.",
        )

    try:
        EmailService.send_contact_email(
            sender_name=payload.name.strip(),
            sender_email=str(payload.email),
            message=payload.message.strip(),
        )
    except Exception as exc:
        print("CONTACT EMAIL ERROR:", repr(exc))

        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="No se pudo enviar el mensaje de contacto.",
        ) from exc

    return ContactMessageResponse(
        status="ok",
        message="Mensaje enviado correctamente.",
    )