from app.domain.interfaces import AnswerGateway
from app.domain.models import Answer


class AskQuestionService:
    def __init__(self, answer_gateway: AnswerGateway) -> None:
        self._answer_gateway = answer_gateway

    def _ignore(self, _: str):
        pass

    async def ask(self, question: str) -> Answer:
        # Question is ignored no avoid headache overhead.
        self._ignore(question)
        return await self._answer_gateway.get_answer()
