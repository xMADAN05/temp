from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.feedback_entity import FeedbackEntity
from ...models.get_observability_user_feedback_response_404 import GetObservabilityUserFeedbackResponse404
from ...models.get_observability_user_feedback_response_500 import GetObservabilityUserFeedbackResponse500
from ...types import Response


def _get_kwargs(
    racfid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/observability/feedback/user/{racfid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[GetObservabilityUserFeedbackResponse404, GetObservabilityUserFeedbackResponse500, list["FeedbackEntity"]]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FeedbackEntity.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 404:
        response_404 = GetObservabilityUserFeedbackResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = GetObservabilityUserFeedbackResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[GetObservabilityUserFeedbackResponse404, GetObservabilityUserFeedbackResponse500, list["FeedbackEntity"]]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    racfid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[GetObservabilityUserFeedbackResponse404, GetObservabilityUserFeedbackResponse500, list["FeedbackEntity"]]
]:
    """Get feedback records by User's RACFID

     Retrieve all feedback records associated with a specific user's RACFID

    Args:
        racfid (str):  Example: A123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetObservabilityUserFeedbackResponse404, GetObservabilityUserFeedbackResponse500, list['FeedbackEntity']]]
    """

    kwargs = _get_kwargs(
        racfid=racfid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    racfid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[GetObservabilityUserFeedbackResponse404, GetObservabilityUserFeedbackResponse500, list["FeedbackEntity"]]
]:
    """Get feedback records by User's RACFID

     Retrieve all feedback records associated with a specific user's RACFID

    Args:
        racfid (str):  Example: A123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetObservabilityUserFeedbackResponse404, GetObservabilityUserFeedbackResponse500, list['FeedbackEntity']]
    """

    return sync_detailed(
        racfid=racfid,
        client=client,
    ).parsed


async def asyncio_detailed(
    racfid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[GetObservabilityUserFeedbackResponse404, GetObservabilityUserFeedbackResponse500, list["FeedbackEntity"]]
]:
    """Get feedback records by User's RACFID

     Retrieve all feedback records associated with a specific user's RACFID

    Args:
        racfid (str):  Example: A123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetObservabilityUserFeedbackResponse404, GetObservabilityUserFeedbackResponse500, list['FeedbackEntity']]]
    """

    kwargs = _get_kwargs(
        racfid=racfid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    racfid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[GetObservabilityUserFeedbackResponse404, GetObservabilityUserFeedbackResponse500, list["FeedbackEntity"]]
]:
    """Get feedback records by User's RACFID

     Retrieve all feedback records associated with a specific user's RACFID

    Args:
        racfid (str):  Example: A123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetObservabilityUserFeedbackResponse404, GetObservabilityUserFeedbackResponse500, list['FeedbackEntity']]
    """

    return (
        await asyncio_detailed(
            racfid=racfid,
            client=client,
        )
    ).parsed
