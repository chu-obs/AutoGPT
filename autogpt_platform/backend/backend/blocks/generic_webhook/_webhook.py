import logging

from fastapi import Request
from strenum import StrEnum

from backend.sdk import Credentials, ManualWebhookManagerBase, Webhook

logger = logging.getLogger(__name__)


class GenericWebhookType(StrEnum):
    PLAIN = "plain"


class GenericWebhooksManager(ManualWebhookManagerBase):
    WebhookType = GenericWebhookType

    @classmethod
    async def validate_payload(
        cls, webhook: Webhook, request: Request, credentials: Credentials | None = None
    ) -> tuple[dict, str]:
        payload = await request.json()
        event_type = GenericWebhookType.PLAIN

        return payload, event_type
