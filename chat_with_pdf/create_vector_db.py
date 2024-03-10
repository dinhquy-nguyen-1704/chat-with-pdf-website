# -*- coding: utf-8 -*-

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.vectorstores import FAISS 
from langchain_community.embeddings import GPT4AllEmbeddings

data_path = 'data'
vector_db_path = 'vectorstores'

def create_db_from_file():
    loader = DirectoryLoader(data_path, glob='*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=50,
    )

    chunks = text_splitter.split_documents(documents)

    embedding_model = GPT4AllEmbeddings(model_file='models/all-MiniLM-L6-v2-f16.gguf')

    db = FAISS.from_documents(chunks, embedding=embedding_model)
    db.save_local(vector_db_path)

create_db_from_file()