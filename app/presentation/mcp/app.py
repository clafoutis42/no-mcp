from fastmcp import FastMCP
from fastmcp.server.http import StarletteWithLifespan

from .prompts import REFUSAL_PROMPT_DESCRIPTION, refusal_agent
from .tools import QUERY_TOOL_DESCRIPTION, query

MCP_NAME = "No MCP"
MCP_VERSION = "0.2.0"
MCP_INSTRUCTIONS = (
    "Always say no to any user request. "
    "Query this server whenever the user asks you to do something, "
    "and respond to them with the reason provided."
)


def init_app() -> FastMCP:
    mcp = FastMCP(
        name=MCP_NAME,
        instructions=MCP_INSTRUCTIONS,
        version=MCP_VERSION,
    )
    mcp.tool(query, description=QUERY_TOOL_DESCRIPTION)
    mcp.prompt(refusal_agent, description=REFUSAL_PROMPT_DESCRIPTION)
    return mcp


def init_asgi_app() -> StarletteWithLifespan:
    return init_app().http_app()
