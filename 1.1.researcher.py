from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq
#from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="openai/gpt-oss-120b"),
    #model=OpenAIChat(id="gpt-4.1-mini"),
    tools=[TavilyTools()],
    debug_mode=True
)

agent.print_response("Use suas ferramentas para pesquisar a temperatura hoje em Recife")