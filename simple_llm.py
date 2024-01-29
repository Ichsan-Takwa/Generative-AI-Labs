import os
from langchain_openai import ChatOpenAI as OpenAI
#from langchain.chat_models import ChatOpenAI
import gradio as gr

# assign API key
os.environ["OPENAI_API_KEY"] = "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"

gpt3 = OpenAI(model_name="gpt-3.5-turbo")

def chatbot(inpt):
    return gpt3.invoke(inpt).content

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch(server_name="0.0.0.0", server_port= 7860)