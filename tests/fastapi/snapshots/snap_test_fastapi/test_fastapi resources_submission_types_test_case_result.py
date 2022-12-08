# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.variable_value import VariableValue
from .actual_result import ActualResult


class TestCaseResult(pydantic.BaseModel):
    expected_result: VariableValue = pydantic.Field(alias="expectedResult")
    actual_result: ActualResult = pydantic.Field(alias="actualResult")
    passed: bool

    class Partial(typing_extensions.TypedDict):
        expected_result: typing_extensions.NotRequired[VariableValue]
        actual_result: typing_extensions.NotRequired[ActualResult]
        passed: typing_extensions.NotRequired[bool]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseResult.Validators.root
            def validate(values: TestCaseResult.Partial) -> TestCaseResult.Partial:
                ...

            @TestCaseResult.Validators.field("expected_result")
            def validate_expected_result(expected_result: VariableValue, values: TestCaseResult.Partial) -> VariableValue:
                ...

            @TestCaseResult.Validators.field("actual_result")
            def validate_actual_result(actual_result: ActualResult, values: TestCaseResult.Partial) -> ActualResult:
                ...

            @TestCaseResult.Validators.field("passed")
            def validate_passed(passed: bool, values: TestCaseResult.Partial) -> bool:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TestCaseResult.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TestCaseResult.Validators._RootValidator]] = []
        _expected_result_pre_validators: typing.ClassVar[
            typing.List[TestCaseResult.Validators.ExpectedResultValidator]
        ] = []
        _expected_result_post_validators: typing.ClassVar[
            typing.List[TestCaseResult.Validators.ExpectedResultValidator]
        ] = []
        _actual_result_pre_validators: typing.ClassVar[
            typing.List[TestCaseResult.Validators.ActualResultValidator]
        ] = []
        _actual_result_post_validators: typing.ClassVar[
            typing.List[TestCaseResult.Validators.ActualResultValidator]
        ] = []
        _passed_pre_validators: typing.ClassVar[typing.List[TestCaseResult.Validators.PassedValidator]] = []
        _passed_post_validators: typing.ClassVar[typing.List[TestCaseResult.Validators.PassedValidator]] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[[TestCaseResult.Validators._RootValidator], TestCaseResult.Validators._RootValidator]:
            def decorator(
                validator: TestCaseResult.Validators._RootValidator,
            ) -> TestCaseResult.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["expected_result"], *, pre: bool = False
        ) -> typing.Callable[
            [TestCaseResult.Validators.ExpectedResultValidator], TestCaseResult.Validators.ExpectedResultValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["actual_result"], *, pre: bool = False
        ) -> typing.Callable[
            [TestCaseResult.Validators.ActualResultValidator], TestCaseResult.Validators.ActualResultValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["passed"], *, pre: bool = False
        ) -> typing.Callable[[TestCaseResult.Validators.PassedValidator], TestCaseResult.Validators.PassedValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "expected_result":
                    if pre:
                        cls._expected_result_pre_validators.append(validator)
                    else:
                        cls._expected_result_post_validators.append(validator)
                if field_name == "actual_result":
                    if pre:
                        cls._actual_result_pre_validators.append(validator)
                    else:
                        cls._actual_result_post_validators.append(validator)
                if field_name == "passed":
                    if pre:
                        cls._passed_pre_validators.append(validator)
                    else:
                        cls._passed_post_validators.append(validator)
                return validator

            return decorator

        class ExpectedResultValidator(typing_extensions.Protocol):
            def __call__(self, __v: VariableValue, __values: TestCaseResult.Partial) -> VariableValue:
                ...

        class ActualResultValidator(typing_extensions.Protocol):
            def __call__(self, __v: ActualResult, __values: TestCaseResult.Partial) -> ActualResult:
                ...

        class PassedValidator(typing_extensions.Protocol):
            def __call__(self, __v: bool, __values: TestCaseResult.Partial) -> bool:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TestCaseResult.Partial) -> TestCaseResult.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: TestCaseResult.Partial) -> TestCaseResult.Partial:
        for validator in TestCaseResult.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: TestCaseResult.Partial) -> TestCaseResult.Partial:
        for validator in TestCaseResult.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("expected_result", pre=True)
    def _pre_validate_expected_result(cls, v: VariableValue, values: TestCaseResult.Partial) -> VariableValue:
        for validator in TestCaseResult.Validators._expected_result_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("expected_result", pre=False)
    def _post_validate_expected_result(cls, v: VariableValue, values: TestCaseResult.Partial) -> VariableValue:
        for validator in TestCaseResult.Validators._expected_result_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("actual_result", pre=True)
    def _pre_validate_actual_result(cls, v: ActualResult, values: TestCaseResult.Partial) -> ActualResult:
        for validator in TestCaseResult.Validators._actual_result_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("actual_result", pre=False)
    def _post_validate_actual_result(cls, v: ActualResult, values: TestCaseResult.Partial) -> ActualResult:
        for validator in TestCaseResult.Validators._actual_result_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("passed", pre=True)
    def _pre_validate_passed(cls, v: bool, values: TestCaseResult.Partial) -> bool:
        for validator in TestCaseResult.Validators._passed_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("passed", pre=False)
    def _post_validate_passed(cls, v: bool, values: TestCaseResult.Partial) -> bool:
        for validator in TestCaseResult.Validators._passed_post_validators:
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
