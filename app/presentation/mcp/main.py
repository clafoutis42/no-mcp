from fastmcp import FastMCP

from app.settings import Settings

from .container import Container

mcp = FastMCP(
    name="No MCP",
    instructions="Universal human question answer machine.",
    version="0.0.1",
)

container = Container()
container.config.from_pydantic(Settings())


@mcp.tool(
    description="Use this tool when a human asks you something. This will indicate what to reply to the human."  # noqa: E501
)
async def query(q: str) -> str:
    ask_question_service = container.ask_question_service()
    answer = await ask_question_service.ask(q)
    return answer.reason


if __name__ == "__main__":
    mcp.run(transport="stdio")
