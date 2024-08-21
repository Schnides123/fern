# This file was auto-generated by Fern from our API Definition.

from seed import SeedCrossPackageTypeNames
from seed import AsyncSeedCrossPackageTypeNames
import typing
from ..utilities import validate_response


async def test_get_direct_thread(
    client: SeedCrossPackageTypeNames, async_client: AsyncSeedCrossPackageTypeNames
) -> None:
    expected_response: typing.Any = {"foo": {}}
    expected_types: typing.Any = {"foo": {}}
    response = client.folder_a.service.get_direct_thread()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.folder_a.service.get_direct_thread()
    validate_response(async_response, expected_response, expected_types)
