"""Reason-code formatting helpers."""
import anthropic

_client = anthropic.Anthropic()

def reason_codes(case: dict) -> list[str]:
    """Turns a case record into short, customer-safe reason codes."""
    reply = _client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=200,
        messages=[{"role": "user", "content": f"List 3 short reason codes for this case: {case}"}],
    )
    return [line.strip("- ").strip() for line in reply.content[0].text.splitlines() if line.strip()]
