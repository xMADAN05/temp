from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.feedback_entity import FeedbackEntity
from ...models.get_observability_application_feedback_response_404 import GetObservabilityApplicationFeedbackResponse404
from ...models.get_observability_application_feedback_response_500 import GetObservabilityApplicationFeedbackResponse500
from ...types import Response


def _get_kwargs(
    application_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/observability/feedback/application/{application_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetObservabilityApplicationFeedbackResponse404,
        GetObservabilityApplicationFeedbackResponse500,
        list["FeedbackEntity"],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FeedbackEntity.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 404:
        response_404 = GetObservabilityApplicationFeedbackResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = GetObservabilityApplicationFeedbackResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetObservabilityApplicationFeedbackResponse404,
        GetObservabilityApplicationFeedbackResponse500,
        list["FeedbackEntity"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    application_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        GetObservabilityApplicationFeedbackResponse404,
        GetObservabilityApplicationFeedbackResponse500,
        list["FeedbackEntity"],
    ]
]:
    """Get feedback records by ApplicationId

     Retrieve all feedback records associated with a specific application

    Args:
        application_id (UUID):  Example: 1309860b-eb8d-4da6-b279-68a4d7c49f7b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetObservabilityApplicationFeedbackResponse404, GetObservabilityApplicationFeedbackResponse500, list['FeedbackEntity']]]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    application_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        GetObservabilityApplicationFeedbackResponse404,
        GetObservabilityApplicationFeedbackResponse500,
        list["FeedbackEntity"],
    ]
]:
    """Get feedback records by ApplicationId

     Retrieve all feedback records associated with a specific application

    Args:
        application_id (UUID):  Example: 1309860b-eb8d-4da6-b279-68a4d7c49f7b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetObservabilityApplicationFeedbackResponse404, GetObservabilityApplicationFeedbackResponse500, list['FeedbackEntity']]
    """

    return sync_detailed(
        application_id=application_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    application_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        GetObservabilityApplicationFeedbackResponse404,
        GetObservabilityApplicationFeedbackResponse500,
        list["FeedbackEntity"],
    ]
]:
    """Get feedback records by ApplicationId

     Retrieve all feedback records associated with a specific application

    Args:
        application_id (UUID):  Example: 1309860b-eb8d-4da6-b279-68a4d7c49f7b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetObservabilityApplicationFeedbackResponse404, GetObservabilityApplicationFeedbackResponse500, list['FeedbackEntity']]]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    application_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        GetObservabilityApplicationFeedbackResponse404,
        GetObservabilityApplicationFeedbackResponse500,
        list["FeedbackEntity"],
    ]
]:
    """Get feedback records by ApplicationId

     Retrieve all feedback records associated with a specific application

    Args:
        application_id (UUID):  Example: 1309860b-eb8d-4da6-b279-68a4d7c49f7b.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetObservabilityApplicationFeedbackResponse404, GetObservabilityApplicationFeedbackResponse500, list['FeedbackEntity']]
    """

    return (
        await asyncio_detailed(
            application_id=application_id,
            client=client,
        )
    ).parsed
