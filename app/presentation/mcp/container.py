from dependency_injector import containers, providers

from app.application.services.ask_question_service import AskQuestionService
from app.infrastructure.gateways.http_answer_gateway import HttpAnswerGateway


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    mcp_run_config = providers.Selector(
        config.MCP_TRANSPORT,
        stdio=providers.Dict(transport="stdio"),
        http=providers.Dict(
            transport="http",
            host=config.MCP_HTTP_HOST,
            port=config.MCP_HTTP_PORT,
            path=config.MCP_HTTP_PATH,
        ),
    )

    ask_question_service = providers.Singleton(
        AskQuestionService,
        providers.Singleton(
            HttpAnswerGateway,
            config.NO_BASE_URL.provided.unicode_string.call(),
        ),
    )
