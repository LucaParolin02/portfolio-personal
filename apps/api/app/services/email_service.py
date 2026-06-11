import smtplib
from email.message import EmailMessage

from app.core.config import settings


class EmailService:
    """
    Servicio responsable de enviar emails.

    Las credenciales SMTP viven únicamente en el backend.
    Nunca deben exponerse al frontend.
    """

    @staticmethod
    def send_contact_email(
        sender_name: str,
        sender_email: str,
        message: str,
    ) -> None:
        email_message = EmailMessage()

        email_message["Subject"] = f"Contacto desde portfolio - {sender_name}"
        email_message["From"] = (
            f"{settings.SMTP_FROM_NAME} <{settings.SMTP_FROM_EMAIL}>"
        )
        email_message["To"] = settings.CONTACT_TARGET_EMAIL
        email_message["Reply-To"] = sender_email

        body = f"""
Nuevo mensaje desde el portfolio.

Nombre:
{sender_name}

Email:
{sender_email}

Mensaje:
{message}
""".strip()

        email_message.set_content(body)

        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            smtp.send_message(email_message)