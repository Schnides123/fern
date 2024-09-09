# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ..commons.problem_id import ProblemId
from .code_execution_update import CodeExecutionUpdate


class SubmissionResponse_ServerInitialized(UniversalBaseModel):
    type: typing.Literal["serverInitialized"] = "serverInitialized"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            extra = pydantic.Extra.allow


class SubmissionResponse_ProblemInitialized(UniversalBaseModel):
    value: ProblemId
    type: typing.Literal["problemInitialized"] = "problemInitialized"


class SubmissionResponse_WorkspaceInitialized(UniversalBaseModel):
    type: typing.Literal["workspaceInitialized"] = "workspaceInitialized"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            extra = pydantic.Extra.allow


class SubmissionResponse_ServerErrored(UniversalBaseModel):
    type: typing.Literal["serverErrored"] = "serverErrored"
    exception_type: str = pydantic.Field(alias="exceptionType")
    exception_message: str = pydantic.Field(alias="exceptionMessage")
    exception_stacktrace: str = pydantic.Field(alias="exceptionStacktrace")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            extra = pydantic.Extra.allow


class SubmissionResponse_CodeExecutionUpdate(UniversalBaseModel):
    value: CodeExecutionUpdate
    type: typing.Literal["codeExecutionUpdate"] = "codeExecutionUpdate"


class SubmissionResponse_Terminated(UniversalBaseModel):
    type: typing.Literal["terminated"] = "terminated"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            extra = pydantic.Extra.allow


SubmissionResponse = typing.Union[
    SubmissionResponse_ServerInitialized,
    SubmissionResponse_ProblemInitialized,
    SubmissionResponse_WorkspaceInitialized,
    SubmissionResponse_ServerErrored,
    SubmissionResponse_CodeExecutionUpdate,
    SubmissionResponse_Terminated,
]
