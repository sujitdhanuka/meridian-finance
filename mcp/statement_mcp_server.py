"""Statement MCP Server — exposes read-only account-statement tools over MCP."""
from mcp.server import Server
from mcp.types import Tool

server = Server("meridian-statements")

@server.tool()
def fetch_statement(account_id: str, month: str) -> dict:
    """Returns the masked monthly statement for an account (read-only)."""
    return {"account_id": account_id[-4:].rjust(len(account_id), "*"), "month": month, "entries": []}

def statement_mcp_server() -> Server:
    return server
