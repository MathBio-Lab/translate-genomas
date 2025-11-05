from fastapi import APIRouter, Depends
from app.core.instance import get_translate_service
from app.schemas.translate_schemas import TranslationRequest
from app.config.aws_client import get_translate_client
from app.utils.responses.response import error_response, success_response

router = APIRouter(prefix="/translate", tags=["routers_translate"])

translate = get_translate_client()


@router.post("/")
async def translate_text(
    request: TranslationRequest, translate_service=Depends(get_translate_service)
):
    """
    Endpoint para traducir texto usando AWS Translate (vía boto3)
    """
    try:
        response = translate_service.translate_text(
            text=request.text,
            source=request.source_language,
            target=request.target_language,
        )
        return success_response(
            data={"translated_text": response},
            message="Traducción realizada exitosamente",
        )
    except Exception as e:
        return error_response(message=str(e), status_code=500)
