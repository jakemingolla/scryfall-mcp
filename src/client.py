import asyncio

from mcp import ClientSession
from mcp.client.sse import sse_client


async def main():
    async with sse_client("http://localhost:8000/sse") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            card = await session.call_tool(
                "get_card",
                arguments={"card_id": "56ebc372-aabd-4174-a943-c7bf59e5028d"},
            )
            print(card)


asyncio.run(main())
