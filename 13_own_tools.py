from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.google import Gemini
#from agno.models.groq import Groq
#from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.os import AgentOS
from agno.db.sqlite import SqliteDb


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


db = SqliteDb(db_file="tmp/agent.db", session_table="agent_session")

agent = Agent(
    name="Agente do tempo",
    model=Gemini(id="gemini-3.8-flash"),
    #model=Groq(id="openai/gpt-oss-120b"),
    #model=OpenAIChat(id="gpt-4.1-mini"),
    tools=[
        TavilyTools(),
        celsius_to_fh,
    ],
    db=db,
    add_history_to_context=True,
    num_history_runs=3,
    #debug_mode=True
)

agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

if __name__=="__main__":
    agent_os.serve(app="13_own_tools:app", reload=True)

#agent.print_response("Use suas ferramentas para pesquisar a temperatura de hoje em Recife e em Camaragibe-PE em Fahrenheit")
