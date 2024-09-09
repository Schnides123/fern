# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .exception_info import ExceptionInfo
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class InternalError(UniversalBaseModel):
    exception_info: ExceptionInfo = pydantic.Field(alias="exceptionInfo")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            extra = pydantic.Extra.allow
