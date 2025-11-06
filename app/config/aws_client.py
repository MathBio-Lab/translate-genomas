import boto3
from app.config.environment import settings


def get_boto3_session() -> boto3.Session:
    """
    Retorna una sesión boto3:
    - En desarrollo: usa claves del .env
    - En producción: usa el Role IAM del entorno (sin tocar las variables)
    """
    if settings.ENVIRONMENT == "development" and settings.AWS_ACCESS_KEY_ID:
        return boto3.Session(
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION,
        )
    else:
        return boto3.Session(region_name=settings.AWS_REGION)


def get_translate_client():
    """Devuelve un cliente listo para usar AWS Translate"""
    session = get_boto3_session()
    return session.client("translate")
