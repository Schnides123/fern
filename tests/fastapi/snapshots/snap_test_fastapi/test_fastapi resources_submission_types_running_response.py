# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .running_submission_state import RunningSubmissionState
from .submission_id import SubmissionId


class RunningResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    state: RunningSubmissionState

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        state: typing_extensions.NotRequired[RunningSubmissionState]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @RunningResponse.Validators.root
            def validate(values: RunningResponse.Partial) -> RunningResponse.Partial:
                ...

            @RunningResponse.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: RunningResponse.Partial) -> SubmissionId:
                ...

            @RunningResponse.Validators.field("state")
            def validate_state(state: RunningSubmissionState, values: RunningResponse.Partial) -> RunningSubmissionState:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[RunningResponse.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[RunningResponse.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[RunningResponse.Validators.SubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[RunningResponse.Validators.SubmissionIdValidator]
        ] = []
        _state_pre_validators: typing.ClassVar[typing.List[RunningResponse.Validators.StateValidator]] = []
        _state_post_validators: typing.ClassVar[typing.List[RunningResponse.Validators.StateValidator]] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[[RunningResponse.Validators._RootValidator], RunningResponse.Validators._RootValidator]:
            def decorator(
                validator: RunningResponse.Validators._RootValidator,
            ) -> RunningResponse.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"], *, pre: bool = False
        ) -> typing.Callable[
            [RunningResponse.Validators.SubmissionIdValidator], RunningResponse.Validators.SubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["state"], *, pre: bool = False
        ) -> typing.Callable[[RunningResponse.Validators.StateValidator], RunningResponse.Validators.StateValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    if pre:
                        cls._submission_id_pre_validators.append(validator)
                    else:
                        cls._submission_id_post_validators.append(validator)
                if field_name == "state":
                    if pre:
                        cls._state_pre_validators.append(validator)
                    else:
                        cls._state_post_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: RunningResponse.Partial) -> SubmissionId:
                ...

        class StateValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: RunningSubmissionState, __values: RunningResponse.Partial
            ) -> RunningSubmissionState:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: RunningResponse.Partial) -> RunningResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: RunningResponse.Partial) -> RunningResponse.Partial:
        for validator in RunningResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: RunningResponse.Partial) -> RunningResponse.Partial:
        for validator in RunningResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: RunningResponse.Partial) -> SubmissionId:
        for validator in RunningResponse.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(cls, v: SubmissionId, values: RunningResponse.Partial) -> SubmissionId:
        for validator in RunningResponse.Validators._submission_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("state", pre=True)
    def _pre_validate_state(cls, v: RunningSubmissionState, values: RunningResponse.Partial) -> RunningSubmissionState:
        for validator in RunningResponse.Validators._state_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("state", pre=False)
    def _post_validate_state(cls, v: RunningSubmissionState, values: RunningResponse.Partial) -> RunningSubmissionState:
        for validator in RunningResponse.Validators._state_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
