from typing import List, Union
from pydantic import BaseModel, ConfigDict


class TranslationRequest(BaseModel):
    """
    Modelo para traducción de uno o varios textos.
    """

    text: Union[str, List[str]]
    source_language: str
    target_language: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "text": [
                    "Hello, how are you?",
                    "This is a sample text for translation.",
                ],
                "source_language": "en",
                "target_language": "es",
            }
        },
    )


class TranslationResponse(BaseModel):
    translated_texts: List[str]
