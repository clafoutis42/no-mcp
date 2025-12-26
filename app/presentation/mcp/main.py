import asyncio

from app.settings import Settings

from .app import init_app
from .container import Container


async def amain():
    container = Container()
    container.config.from_pydantic(Settings())
    container.wire(packages=["."])

    mcp = init_app()
    await mcp.run_async(**container.mcp_run_config())


def main():
    asyncio.run(amain())


if __name__ == "__main__":
    main()
