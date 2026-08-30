from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.tools.yfinance import YFinanceTools
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="openai/gpt-oss-120b"),
    tools=[YFinanceTools()],
    instructions="Use tabelas para mostrar a informação final. Não inclua nenhum outro texto."
)

agent.print_response("Qual a cotação atual das 10 empresas mais valiosas do planeta?", stream=True)