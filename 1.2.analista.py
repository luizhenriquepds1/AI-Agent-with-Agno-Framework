from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.tools.yfinance import YFinanceTools
from agno.models.google import Gemini
#from agno.models.groq import Groq
#from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Gemini(id="gemini-3.8-flash"),
    #model=Groq(id="openai/gpt-oss-120b"),
    #model=OpenAIChat(id="gpt-4.1-mini"),
    tools=[YFinanceTools()],
    instructions="Use tabelas para mostrar a informação final. Não inclua nenhum outro texto."
)

agent.print_response("Qual a cotação atual das 10 empresas mais valiosas do planeta?", stream=True)
