# This file was auto-generated by Fern from our API Definition.

from seed.client import AsyncSeedVariables, SeedVariables


async def test_post(client: SeedVariables, async_client: AsyncSeedVariables) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.service.post(endpoint_param="string") is None  # type: ignore[func-returns-value]

    assert await async_client.service.post(endpoint_param="string") is None  # type: ignore[func-returns-value]