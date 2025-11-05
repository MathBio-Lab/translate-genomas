import asyncio
from botocore.exceptions import BotoCoreError, ClientError
import concurrent.futures
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

    async def translate_batch_async(self, texts, source, target):
        loop = asyncio.get_running_loop()
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
            tasks = [
                loop.run_in_executor(pool, self.translate_text, text, source, target)
                for text in texts
            ]
            return await asyncio.gather(*tasks)
