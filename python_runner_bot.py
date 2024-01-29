import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI 

openai_api_key = "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"

os.environ["OPENAI_API_KEY"] = openai_api_key

gpt3 = OpenAI(model_name='gpt-3.5-turbo')

# Equipting the agent with some tools
tools = load_tools([ "llm-math", "python_repl","requests_all","human"], llm=gpt3)

# Defining the agent
agent = initialize_agent(tools, llm=gpt3, agent="zero-shot-react-description", verbose=True)
agent.run("create simple matplotlib showing sin function and plot it")