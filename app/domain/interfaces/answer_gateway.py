from typing import Protocol

from app.domain.models import Answer


class AnswerGateway(Protocol):
    async def get_answer(self) -> Answer: ...
