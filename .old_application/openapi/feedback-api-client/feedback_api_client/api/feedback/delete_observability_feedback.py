from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_observability_feedback_response_404 import DeleteObservabilityFeedbackResponse404
from ...models.delete_observability_feedback_response_500 import DeleteObservabilityFeedbackResponse500
from ...types import Response


def _get_kwargs(
    feedback_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/v1/observability/feedback/{feedback_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DeleteObservabilityFeedbackResponse404, DeleteObservabilityFeedbackResponse500]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 404:
        response_404 = DeleteObservabilityFeedbackResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = DeleteObservabilityFeedbackResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DeleteObservabilityFeedbackResponse404, DeleteObservabilityFeedbackResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    feedback_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, DeleteObservabilityFeedbackResponse404, DeleteObservabilityFeedbackResponse500]]:
    """Delete a recorded feedback

     Delete a recorded feedback by its unique identifier

    Args:
        feedback_id (UUID):  Example: 1309860b-eb8d-4da6-b279-68a4d7c49f7b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteObservabilityFeedbackResponse404, DeleteObservabilityFeedbackResponse500]]
    """

    kwargs = _get_kwargs(
        feedback_id=feedback_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    feedback_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, DeleteObservabilityFeedbackResponse404, DeleteObservabilityFeedbackResponse500]]:
    """Delete a recorded feedback

     Delete a recorded feedback by its unique identifier

    Args:
        feedback_id (UUID):  Example: 1309860b-eb8d-4da6-b279-68a4d7c49f7b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteObservabilityFeedbackResponse404, DeleteObservabilityFeedbackResponse500]
    """

    return sync_detailed(
        feedback_id=feedback_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    feedback_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, DeleteObservabilityFeedbackResponse404, DeleteObservabilityFeedbackResponse500]]:
    """Delete a recorded feedback

     Delete a recorded feedback by its unique identifier

    Args:
        feedback_id (UUID):  Example: 1309860b-eb8d-4da6-b279-68a4d7c49f7b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteObservabilityFeedbackResponse404, DeleteObservabilityFeedbackResponse500]]
    """

    kwargs = _get_kwargs(
        feedback_id=feedback_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    feedback_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, DeleteObservabilityFeedbackResponse404, DeleteObservabilityFeedbackResponse500]]:
    """Delete a recorded feedback

     Delete a recorded feedback by its unique identifier

    Args:
        feedback_id (UUID):  Example: 1309860b-eb8d-4da6-b279-68a4d7c49f7b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteObservabilityFeedbackResponse404, DeleteObservabilityFeedbackResponse500]
    """

    return (
        await asyncio_detailed(
            feedback_id=feedback_id,
            client=client,
        )
    ).parsed
