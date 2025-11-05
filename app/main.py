from fastapi import FastAPI, Request
from app.core.exceptions import AlreadyExistsException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic_core import ValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

# ---------- APP CONTROLLERS ----------
from app.controllers.translate_controller import router as translate_router


app = FastAPI()

# ---------- APP ROUTERS ----------
app.include_router(translate_router)


# ---------- API ERROR ----------
@app.exception_handler(AlreadyExistsException)
async def already_exists_exception_handler(request, exc: AlreadyExistsException):
    return JSONResponse(
        status_code=409,  # Conflict
        content={"detail": exc.message},
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    # Si es un 404 (ruta no encontrada)
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": "La ruta solicitada no existe o no fue encontrada.",
                "errors": [f"Ruta: {request.url.path}"],
                "data": None,
            },
        )
    # Para otros HTTPException (403, 401, etc.)
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail or "Error HTTP",
            "errors": [exc.detail] if exc.detail else None,
            "data": None,
        },
    )


@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    errors = []
    for err in exc.errors():
        loc = ".".join([str(l) for l in err["loc"] if l != "body"])
        msg = err.get("msg", "Error de validación")
        if loc:
            errors.append(f"{loc}: {msg}")
        else:
            errors.append(msg)

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": errors[0], 
            "errors": errors, 
            "data": None,
        },
    )


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    first_error = exc.errors()[0]
    error_message = first_error.get("msg", "Error de validación")
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": error_message,
            "data": None,
        },
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
