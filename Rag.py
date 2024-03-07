import streamlit as st
import pandas as pd
import numpy as np
from st_chat_message import message
import fitz 
from dotenv import load_dotenv
load_dotenv()
from utils import openaikey


from raptor.raptor.raptor import RetrievalAugmentation

RA = RetrievalAugmentation()

def upload_document():
    uploaded_files= st.file_uploader("Upload a file", type=["csv", "xlsx","pdf", "XML"])
    if uploaded_files :
        st.success("File has been uploaded")
        
        file_content = " "
        
        
        
        if uploaded_files.type == "text/plain":
            file_content= uploaded_files .read().decode('utf-8')
        elif uploaded_files.type == "application/pdf":
            with fitz.open("pdf", stream=uploaded_files.getvalue()) as doc:
                texts=[page.get_text() for page in doc]
            file_content = " ".join(texts)
      
        RA.add_documents(file_content)
        
        st.spinner("Creating your document input...")
        chat_interface()
        
def chat_interface():
    message("I am your AI assistant. Ask any question about the documents uploaded you want.")

    user_input = st.text_input("Enter your message here")
    
    if user_input:
        message(user_input, is_user=True)
        answer= RA.answer_question(question=user_input)
        message(answer)
        

def main():
    st.title("Raptor AI")
    st.subheader("AI assistant for document analysis using recursive Abstractive Processing for Tree Organized Retrieval")
    upload_document()

if __name__ == "__main__":
    main()

    import logging

