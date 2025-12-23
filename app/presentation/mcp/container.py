from dependency_injector import containers, providers

from app.application.services.ask_question_service import AskQuestionService
from app.infrastructure.gateways.http_answer_gateway import HttpAnswerGateway


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    ask_question_service = providers.Singleton(
        AskQuestionService,
        providers.Singleton(
            HttpAnswerGateway,
            config.NO_BASE_URL.provided.unicode_string.call(),
        ),
    )
