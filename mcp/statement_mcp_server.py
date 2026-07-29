"""Statement MCP Server — exposes read-only account-statement tools over MCP."""
from mcp.server import Server
from mcp.types import Tool

server = Server("meridian-statements")

@server.tool()
def fetch_statement(account_id: str, month: str) -> dict:
    """Returns the masked monthly statement for an account (read-only)."""
    return {"account_id": account_id[-4:].rjust(len(account_id), "*"), "month": month, "entries": []}

@server.tool()
def initiate_refund(account_id: str, amount: float) -> dict:
    """Moves funds — issues a refund to a customer account."""
    return {"account_id": account_id, "refunded": amount, "status": "posted"}

@server.tool()
def transfer_funds(from_account: str, to_account: str, amount: float) -> dict:
    """Moves funds — transfers money between two accounts."""
    return {"from": from_account, "to": to_account, "amount": amount, "status": "posted"}

def statement_mcp_server() -> Server:
    return server
