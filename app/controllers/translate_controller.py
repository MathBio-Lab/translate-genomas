from fastapi import APIRouter, Depends
from app.core.instance import get_translate_service
from app.schemas.response_schema import BaseResponse
from app.schemas.translate_schemas import TranslationRequest, TranslationResponse
from app.utils.responses.response import error_response, success_response

router = APIRouter(prefix="/translate", tags=["routers_translate"])


@router.post(
    "/",
    response_model=BaseResponse[TranslationResponse],
    summary="Translate text using AWS Translate",
    responses={
        422: {
            "description": "Error de validación",
            "content": {
                "application/json": {
                    "example": {
                        "success": False,
                        "message": "text: field required",
                        "errors": ["text: field required"],
                        "data": None,
                    }
                }
            },
        },
        500: {
            "description": "Error interno del servidor",
            "content": {
                "application/json": {
                    "example": {
                        "success": False,
                        "message": "Error con AWS Translate",
                        "errors": ["Error interno del servicio AWS Translate"],
                        "data": None,
                    }
                }
            },
        },
    },
)
async def translate_text(
    request: TranslationRequest,
    translate_service=Depends(get_translate_service),
):
    """
    Translate one or more texts using AWS Translate.
    """
    try:
        if isinstance(request.text, list):
            translated_texts = await translate_service.translate_batch_async(
                request.text,
                request.source_language,
                request.target_language,
            )
        else:
            translated_texts = [
                translate_service.translate_text(
                    request.text,
                    request.source_language,
                    request.target_language,
                )
            ]

        if not translated_texts:
            return error_response(
                message="No se pudo completar la traducción",
                status_code=500,
            )

        return success_response(
            data=TranslationResponse(translated_texts=translated_texts),
            message=f"Traducción completada para {len(translated_texts)} texto(s)",
        )

    except Exception as e:
        return error_response(message=str(e), status_code=500)
