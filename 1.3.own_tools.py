from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq
#from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

def celsius_to_fh(temperatura_celsius: float):
    """
    Converte temperatura de Celsius para Fahrenheit.

    Args:
        temperatura_celsius (float): Temperatura em grau Celsius

    Returns:
        float: Temperatura convertida para Fahrenheit
    """
    return (temperatura_celsius * 9/5) + 32

agent = Agent(
    model=Groq(id="openai/gpt-oss-120b"),
    #model=OpenAIChat(id="gpt-4.1-mini"),
    tools=[
        TavilyTools(),
        celsius_to_fh,
    ],
    debug_mode=True
)

agent.print_response("Use suas ferramentas para pesquisar a temperatura de hoje em Recife e em Camaragibe-PE em Fahrenheit")