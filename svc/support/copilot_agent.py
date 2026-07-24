"""Support Copilot — agent that drafts responses to customer service tickets."""
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

SYSTEM_PROMPT = """You are Meridian Finance's support copilot.
Answer only from the knowledge base. Never quote interest rates from memory.
If the customer mentions hardship or harassment, escalate to a human agent immediately."""

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
prompt = ChatPromptTemplate.from_messages([("system", SYSTEM_PROMPT), ("human", "{ticket}")])

def copilot_agent(tools: list) -> AgentExecutor:
    """Builds the ticket-drafting agent with the CRM + KB tools."""
    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, max_iterations=4)
