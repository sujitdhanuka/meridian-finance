"""Fraud Graph — transaction-ring detection over the payments graph."""
import openai
import networkx as nx

def fraud_graph(txn_ring: nx.Graph) -> dict:
    """Flags suspicious transaction rings; drafts the analyst narrative with an LLM."""
    suspicion = sum(d.get("weight", 0) for _, _, d in txn_ring.edges(data=True)) / max(txn_ring.size(), 1)
    narrative = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{
            "role": "user",
            "content": "Summarise why this transaction ring looks suspicious for the fraud analyst: " + str(list(txn_ring.edges)),
        }],
    )
    return {"suspicion": suspicion, "analyst_note": narrative.choices[0].message.content}
