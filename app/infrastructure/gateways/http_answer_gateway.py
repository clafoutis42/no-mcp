from httpx import AsyncClient

from app.domain.models import Answer


class HttpAnswerGateway:
    NO_PATH = "/no"

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self._client = AsyncClient(base_url=base_url)

    async def get_answer(self) -> Answer:
        resp = await self._client.get(self.NO_PATH)
        resp.raise_for_status()
        return Answer(**resp.json())
