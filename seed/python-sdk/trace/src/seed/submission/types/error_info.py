# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .compile_error import CompileError
from .internal_error import InternalError
from .runtime_error import RuntimeError


class ErrorInfo_CompileError(CompileError):
    type: typing.Literal["compileError"] = "compileError"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ErrorInfo_RuntimeError(RuntimeError):
    type: typing.Literal["runtimeError"] = "runtimeError"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ErrorInfo_InternalError(InternalError):
    type: typing.Literal["internalError"] = "internalError"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


ErrorInfo = typing.Union[ErrorInfo_CompileError, ErrorInfo_RuntimeError, ErrorInfo_InternalError]