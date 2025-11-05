from botocore.exceptions import BotoCoreError, ClientError
from app.config.aws_client import get_translate_client


class TranslateService:
    def __init__(self):
        self.client = get_translate_client()

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
