# Importa a classe principal do Agno, usada para criar um agente
from agno.agent import Agent
# Ferramenta pronta que dá ao agente a capacidade de pesquisar na internet (via Tavily)
from agno.tools.tavily import TavilyTools
# "Motor" do agente: o provedor de modelo de linguagem (Gemini, do Google)
from agno.models.google import Gemini
#from agno.models.groq import Groq
#from agno.models.openai import OpenAIChat
# Função que lê o arquivo .env e carrega as chaves secretas como variáveis de ambiente
from dotenv import load_dotenv

# Carrega as chaves (GOOGLE_API_KEY, TAVILY_API_KEY) do .env para o ambiente
load_dotenv()

# Monta o agente: define o modelo que ele usa e as ferramentas que ele pode acionar
agent = Agent(
    model=Gemini(id="gemini-3.8-flash"),
    #model=Groq(id="openai/gpt-oss-120b"),
    #model=OpenAIChat(id="gpt-4.1-mini"),
    tools=[TavilyTools()],
    debug_mode=True  # liga logs extras para ver o "raciocínio"/chamadas de ferramenta do agente
)

# Envia uma pergunta ao agente e imprime a resposta no terminal
agent.print_response("Use suas ferramentas para pesquisar a temperatura hoje em Recife")
