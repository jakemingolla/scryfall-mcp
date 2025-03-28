from mcp.server.fastmcp import FastMCP

from src.api.cards import get_card as api_get_card
from src.api.types import Card, CardId

mcp = FastMCP("scryfall-mcp")


@mcp.tool()
async def get_card(card_id: CardId) -> Card:
    print(f"get_card({card_id})")
    return await api_get_card(card_id)


if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="sse")
    print("MCP server stopped.")
