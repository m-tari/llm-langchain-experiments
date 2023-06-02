from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv("../../.env")  # take environment variables from .env.

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

tools = load_tools(["ddg-search", "llm-math", "python_repl"], llm=llm)

os.environ["LANGCHAIN_TRACING"] = "true"
agent_executer = initialize_agent(tools, llm, 
                                  agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, 
                                  handle_parsing_errors=True,
                                  verbose=True)

agent_executer.run(
    "Find the name of top five singer with most listeners in Canada in the past "
    "year and save it in top_singers.txt"
)