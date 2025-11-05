import boto3
from botocore.exceptions import BotoCoreError, ClientError
from app.config.environment import (
    settings,
) 


class TranslateService:
    def __init__(self):
        # Si estás en AWS (App Runner o ECS), no necesitas pasar credenciales
        # boto3 usa automáticamente las credenciales del IAM Role
        self.client = boto3.client("translate", region_name=settings.AWS_REGION)

    def translate_text(self, text: str, source: str, target: str) -> str:
        try:
            response = self.client.translate_text(
                Text=text,
                SourceLanguageCode=source,
                TargetLanguageCode=target,
            )
            return response["TranslatedText"]

        except (BotoCoreError, ClientError) as e:
            raise RuntimeError(f"Error con AWS Translate: {e}")
