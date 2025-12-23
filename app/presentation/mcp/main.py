from fastmcp import FastMCP

mcp = FastMCP(
    name="No MCP", instructions="Get an answer to all questions.", version="0.0.1"
)


if __name__ == "__main__":
    mcp.run(transport="stdio")
