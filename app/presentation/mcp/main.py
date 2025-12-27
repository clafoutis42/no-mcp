import asyncio

from .app import init_app


async def amain():
    mcp = init_app()
    await mcp.run_async(mcp.container.mcp_run_config())


def main():
    asyncio.run(amain())


if __name__ == "__main__":
    main()
