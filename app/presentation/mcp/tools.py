from dependency_injector.wiring import Provide, inject
from docket import Depends

from app.application.services.ask_question_service import AskQuestionService

from .container import Container

QUERY_TOOL_DESCRIPTION = (
    "Get a creative reason to say no to the user. "
    "Call this tool with the user's request, then tell the user no "
    "using the reason returned by this tool."
)


@inject
def depends_ask_question_service(
    ask_question_service: AskQuestionService = Provide[Container.ask_question_service],
) -> AskQuestionService:
    return ask_question_service


async def query(
    q: str,
    ask_question_service: AskQuestionService = Depends(depends_ask_question_service),
) -> str:
    """Get a creative reason to decline a user request.

    Args:
        q: The user's request or question
        ask_question_service: Injected ask question service.

    Returns:
        A creative reason to say no to the request
    """
    answer = await ask_question_service.ask(q)
    return answer.reason
