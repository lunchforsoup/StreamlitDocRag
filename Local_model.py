import streamlit as st
import pandas as pd
import numpy as np
from st_chat_message import message
import fitz 
from dotenv import load_dotenv
load_dotenv()
from utils import openaikey

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, VectorStoreIndex

model_name="BAAI/bge-small-en-v1.5"
embedding = HuggingFaceEmbedding(model_name, device='cuda')


Settings.embed_model= embedding

index= VectorStoreIndex.from_documents

qa_prompt_tmpl_str =  (
    """context information is below
       ----------------------------
       {context_str}
       ----------------------------
       Given the above context, I want you to think
       step-by-step and answer the following questions. 
       Focus on the actions and key points. In case you 
       do not know say 'I don't know'.
       Query : {query}
       Answer : )
        """
)

qa_prompt_tmpl = PromptTemplate(qa_prompt_tmpl_str)
query_engine.update_prompts({"response_synthesizer:text_qa_template": qa_prompt_tmpl})

response = query_engine.query('What is this repository about?')
print(response)
