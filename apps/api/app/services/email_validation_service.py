import dns.resolver


class EmailValidationService:
    """
    Validaciones adicionales para emails recibidos desde el formulario.

    No garantiza que la casilla exacta exista, pero evita muchos correos falsos
    o dominios inválidos.
    """

    DISPOSABLE_DOMAINS = {
        "mailinator.com",
        "tempmail.com",
        "temp-mail.org",
        "10minutemail.com",
        "guerrillamail.com",
        "yopmail.com",
        "trashmail.com",
    }

    @classmethod
    def validate_email_domain(cls, email: str) -> tuple[bool, str | None]:
        domain = email.split("@")[-1].lower().strip()

        if domain in cls.DISPOSABLE_DOMAINS:
            return False, "No se permiten correos temporales."

        if "." not in domain:
            return False, "El dominio del email no es válido."

        try:
            mx_records = dns.resolver.resolve(domain, "MX")

            if len(mx_records) == 0:
                return False, "El dominio del email no puede recibir correos."

        except dns.resolver.NXDOMAIN:
            return False, "El dominio del email no existe."
        except dns.resolver.NoAnswer:
            return False, "El dominio del email no tiene registros de correo."
        except dns.resolver.NoNameservers:
            return False, "No se pudo validar el dominio del email."
        except dns.exception.Timeout:
            return False, "La validación del email tardó demasiado."
        except Exception:
            return False, "No se pudo validar el email."

        return True, None