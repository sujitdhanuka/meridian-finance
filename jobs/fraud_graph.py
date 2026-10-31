"""Nightly batch run of the fraud-graph model over the previous day's payment rings."""
import openai
import networkx as nx

def fraud_graph(rings: list[nx.Graph]) -> list[dict]:
    """Batch variant used by the 03:00 IST fraud sweep; drafts analyst notes in bulk."""
    out = []
    for ring in rings:
        suspicion = sum(d.get("weight", 0) for _, _, d in ring.edges(data=True)) / max(ring.size(), 1)
        note = openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "Explain this suspicious ring: " + str(list(ring.edges))}],
        )
        out.append({"suspicion": suspicion, "analyst_note": note.choices[0].message.content})
    return out
