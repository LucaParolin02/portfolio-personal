from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, str]:
    """
    Endpoint simple para verificar que la API está viva.

    Este endpoint después nos va a servir para:
    - validar despliegues;
    - probar NGINX;
    - monitorear el backend;
    - diagnosticar problemas en producción.
    """

    return {
        "status": "ok",
        "service": "portfolio-api",
    }