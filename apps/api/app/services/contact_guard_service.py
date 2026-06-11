import time
from collections import defaultdict, deque


class ContactGuardService:
    """
    Protección básica anti-abuso para el formulario de contacto.

    Esta versión usa memoria local del proceso.
    Para producción multi-instancia convendría Redis, PostgreSQL o un servicio externo.
    """

    MIN_FORM_SECONDS = 4
    MAX_REQUESTS_PER_WINDOW = 3
    WINDOW_SECONDS = 15 * 60

    _requests_by_ip: dict[str, deque[float]] = defaultdict(deque)

    @classmethod
    def validate_honeypot(cls, company_website: str | None) -> bool:
        """
        Si el campo oculto viene con valor, probablemente es bot.
        """

        return company_website is None or company_website.strip() == ""

    @classmethod
    def validate_elapsed_time(cls, form_started_at: int) -> bool:
        """
        Evita envíos demasiado rápidos.

        form_started_at llega desde el frontend en milisegundos.
        """

        now_ms = int(time.time() * 1000)
        elapsed_seconds = (now_ms - form_started_at) / 1000

        return elapsed_seconds >= cls.MIN_FORM_SECONDS

    @classmethod
    def is_allowed_ip(cls, ip_address: str) -> bool:
        """
        Permite como máximo N intentos por IP dentro de una ventana de tiempo.
        """

        now = time.time()
        request_times = cls._requests_by_ip[ip_address]

        while request_times and now - request_times[0] > cls.WINDOW_SECONDS:
            request_times.popleft()

        if len(request_times) >= cls.MAX_REQUESTS_PER_WINDOW:
            return False

        request_times.append(now)
        return True