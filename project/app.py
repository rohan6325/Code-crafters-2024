import os
import pickle
from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub



load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
def get_conversation_chain(vectorstore):
    llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vectorstore.as_retriever(), memory=memory)
    return conversation_chain

def handle_userinput(user_question):
    custom_prompt_template = """
    Use the following pieces of information to answer the user's question.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    Context: {context}
    Question: {question}

    Only return the helpful answer below and nothing else.
    Helpful answer:
    """
    context = ""  
    prompt = custom_prompt_template.format(context=context, question=user_question)
    
    response = st.session_state.conversation({'question': prompt})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
def model():
    if os.path.exists('vectorstore.pkl'):
        with open('vectorstore.pkl', 'rb') as f:
            vectorstore = pickle.load(f)
    else:
        text = ""
        with open('env.pdf', 'rb') as pdf_docs:
            pdf_reader = PdfReader(pdf_docs)
            for page in pdf_reader.pages:
                text += page.extract_text()

        text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
        chunks = text_splitter.split_text(text)

        embeddings = HuggingFaceInstructEmbeddings(model_name="impira/layoutlm-document-qa")
        vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)

        with open('vectorstore.pkl', 'wb') as f:
            pickle.dump(vectorstore, f)

    return vectorstore

def main():
    vectorstore = model()
    st.set_page_config(page_title="Env expert", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with your environment expert")
    user_question = st.text_input("Ask a question:")
    if user_question:
        st.session_state.conversation = get_conversation_chain(vectorstore)
        handle_userinput(user_question)
        st.session_state.conversation = get_conversation_chain(vectorstore)

if __name__ == '__main__':
    main()