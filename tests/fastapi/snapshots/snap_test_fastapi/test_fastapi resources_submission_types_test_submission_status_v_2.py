# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.problem_id import ProblemId
from ...v_2.problem.types.problem_info_v_2 import ProblemInfoV2
from .test_submission_update import TestSubmissionUpdate


class TestSubmissionStatusV2(pydantic.BaseModel):
    updates: typing.List[TestSubmissionUpdate]
    problem_id: ProblemId = pydantic.Field(alias="problemId")
    problem_version: int = pydantic.Field(alias="problemVersion")
    problem_info: ProblemInfoV2 = pydantic.Field(alias="problemInfo")

    class Partial(typing_extensions.TypedDict):
        updates: typing_extensions.NotRequired[typing.List[TestSubmissionUpdate]]
        problem_id: typing_extensions.NotRequired[ProblemId]
        problem_version: typing_extensions.NotRequired[int]
        problem_info: typing_extensions.NotRequired[ProblemInfoV2]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestSubmissionStatusV2.Validators.root
            def validate(values: TestSubmissionStatusV2.Partial) -> TestSubmissionStatusV2.Partial:
                ...

            @TestSubmissionStatusV2.Validators.field("updates")
            def validate_updates(updates: typing.List[TestSubmissionUpdate], values: TestSubmissionStatusV2.Partial) -> typing.List[TestSubmissionUpdate]:
                ...

            @TestSubmissionStatusV2.Validators.field("problem_id")
            def validate_problem_id(problem_id: ProblemId, values: TestSubmissionStatusV2.Partial) -> ProblemId:
                ...

            @TestSubmissionStatusV2.Validators.field("problem_version")
            def validate_problem_version(problem_version: int, values: TestSubmissionStatusV2.Partial) -> int:
                ...

            @TestSubmissionStatusV2.Validators.field("problem_info")
            def validate_problem_info(problem_info: ProblemInfoV2, values: TestSubmissionStatusV2.Partial) -> ProblemInfoV2:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TestSubmissionStatusV2.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TestSubmissionStatusV2.Validators._RootValidator]] = []
        _updates_pre_validators: typing.ClassVar[typing.List[TestSubmissionStatusV2.Validators.UpdatesValidator]] = []
        _updates_post_validators: typing.ClassVar[typing.List[TestSubmissionStatusV2.Validators.UpdatesValidator]] = []
        _problem_id_pre_validators: typing.ClassVar[
            typing.List[TestSubmissionStatusV2.Validators.ProblemIdValidator]
        ] = []
        _problem_id_post_validators: typing.ClassVar[
            typing.List[TestSubmissionStatusV2.Validators.ProblemIdValidator]
        ] = []
        _problem_version_pre_validators: typing.ClassVar[
            typing.List[TestSubmissionStatusV2.Validators.ProblemVersionValidator]
        ] = []
        _problem_version_post_validators: typing.ClassVar[
            typing.List[TestSubmissionStatusV2.Validators.ProblemVersionValidator]
        ] = []
        _problem_info_pre_validators: typing.ClassVar[
            typing.List[TestSubmissionStatusV2.Validators.ProblemInfoValidator]
        ] = []
        _problem_info_post_validators: typing.ClassVar[
            typing.List[TestSubmissionStatusV2.Validators.ProblemInfoValidator]
        ] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[
            [TestSubmissionStatusV2.Validators._RootValidator], TestSubmissionStatusV2.Validators._RootValidator
        ]:
            def decorator(
                validator: TestSubmissionStatusV2.Validators._RootValidator,
            ) -> TestSubmissionStatusV2.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["updates"], *, pre: bool = False
        ) -> typing.Callable[
            [TestSubmissionStatusV2.Validators.UpdatesValidator], TestSubmissionStatusV2.Validators.UpdatesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_id"], *, pre: bool = False
        ) -> typing.Callable[
            [TestSubmissionStatusV2.Validators.ProblemIdValidator], TestSubmissionStatusV2.Validators.ProblemIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_version"], *, pre: bool = False
        ) -> typing.Callable[
            [TestSubmissionStatusV2.Validators.ProblemVersionValidator],
            TestSubmissionStatusV2.Validators.ProblemVersionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_info"], *, pre: bool = False
        ) -> typing.Callable[
            [TestSubmissionStatusV2.Validators.ProblemInfoValidator],
            TestSubmissionStatusV2.Validators.ProblemInfoValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "updates":
                    if pre:
                        cls._updates_pre_validators.append(validator)
                    else:
                        cls._updates_post_validators.append(validator)
                if field_name == "problem_id":
                    if pre:
                        cls._problem_id_pre_validators.append(validator)
                    else:
                        cls._problem_id_post_validators.append(validator)
                if field_name == "problem_version":
                    if pre:
                        cls._problem_version_pre_validators.append(validator)
                    else:
                        cls._problem_version_post_validators.append(validator)
                if field_name == "problem_info":
                    if pre:
                        cls._problem_info_pre_validators.append(validator)
                    else:
                        cls._problem_info_post_validators.append(validator)
                return validator

            return decorator

        class UpdatesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[TestSubmissionUpdate], __values: TestSubmissionStatusV2.Partial
            ) -> typing.List[TestSubmissionUpdate]:
                ...

        class ProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: ProblemId, __values: TestSubmissionStatusV2.Partial) -> ProblemId:
                ...

        class ProblemVersionValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: TestSubmissionStatusV2.Partial) -> int:
                ...

        class ProblemInfoValidator(typing_extensions.Protocol):
            def __call__(self, __v: ProblemInfoV2, __values: TestSubmissionStatusV2.Partial) -> ProblemInfoV2:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TestSubmissionStatusV2.Partial) -> TestSubmissionStatusV2.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: TestSubmissionStatusV2.Partial) -> TestSubmissionStatusV2.Partial:
        for validator in TestSubmissionStatusV2.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: TestSubmissionStatusV2.Partial) -> TestSubmissionStatusV2.Partial:
        for validator in TestSubmissionStatusV2.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("updates", pre=True)
    def _pre_validate_updates(
        cls, v: typing.List[TestSubmissionUpdate], values: TestSubmissionStatusV2.Partial
    ) -> typing.List[TestSubmissionUpdate]:
        for validator in TestSubmissionStatusV2.Validators._updates_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("updates", pre=False)
    def _post_validate_updates(
        cls, v: typing.List[TestSubmissionUpdate], values: TestSubmissionStatusV2.Partial
    ) -> typing.List[TestSubmissionUpdate]:
        for validator in TestSubmissionStatusV2.Validators._updates_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_id", pre=True)
    def _pre_validate_problem_id(cls, v: ProblemId, values: TestSubmissionStatusV2.Partial) -> ProblemId:
        for validator in TestSubmissionStatusV2.Validators._problem_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_id", pre=False)
    def _post_validate_problem_id(cls, v: ProblemId, values: TestSubmissionStatusV2.Partial) -> ProblemId:
        for validator in TestSubmissionStatusV2.Validators._problem_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_version", pre=True)
    def _pre_validate_problem_version(cls, v: int, values: TestSubmissionStatusV2.Partial) -> int:
        for validator in TestSubmissionStatusV2.Validators._problem_version_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_version", pre=False)
    def _post_validate_problem_version(cls, v: int, values: TestSubmissionStatusV2.Partial) -> int:
        for validator in TestSubmissionStatusV2.Validators._problem_version_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_info", pre=True)
    def _pre_validate_problem_info(cls, v: ProblemInfoV2, values: TestSubmissionStatusV2.Partial) -> ProblemInfoV2:
        for validator in TestSubmissionStatusV2.Validators._problem_info_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_info", pre=False)
    def _post_validate_problem_info(cls, v: ProblemInfoV2, values: TestSubmissionStatusV2.Partial) -> ProblemInfoV2:
        for validator in TestSubmissionStatusV2.Validators._problem_info_post_validators:
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
