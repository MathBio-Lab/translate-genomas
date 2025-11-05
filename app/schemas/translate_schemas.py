from pydantic import BaseModel

class TranslationRequest(BaseModel):
    """
    Models the request body for translation.
    """

    text: str
    source_language: str
    target_language: str

