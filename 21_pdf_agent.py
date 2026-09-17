from agno.agent import Agent
from agno.models.google import Gemini
#from agno.models.groq import Groq
#from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.os import AgentOS
from agno.db.sqlite import SqliteDb
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.chroma import ChromaDb
from agno.knowledge.embedder.fastembed import FastEmbedEmbedder

load_dotenv()

vector_db = ChromaDb(
    collection="pdf_agent", 
    path="tmp/chromadb", 
    persistent_client=True, 
    embedder=FastEmbedEmbedder(),
)

knowledge = Knowledge(vector_db=vector_db, max_results=3)
knowledge.insert(path="ENGENHARIA+DE+PROMPT.pdf")

agent = Agent(
    name="Agente de PDF",
    model=Gemini(id="gemini-3.8-flash"),
    #model=Groq(id="openai/gpt-oss-120b"),
    knowledge=knowledge,
    search_knowledge=True,
    add_history_to_context=True,
    num_history_runs=4,
)

agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

if __name__=="__main__":
    agent_os.serve(app="21_pdf_agent:app", reload=True)
