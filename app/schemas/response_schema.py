from typing import Generic, TypeVar, Optional
from pydantic.generics import GenericModel

T = TypeVar("T")


class BaseResponse(GenericModel, Generic[T]):
    success: bool
    message: str
    data: Optional[T] = None
