from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS

def load_llm(model_file):
    llm = CTransformers(
        model=model_file,
        model_type='llama',
        max_new_tokens=1024,
        temperature=0.01
    )
    return llm


def create_prompt(template):
    prompt = PromptTemplate(template=template, input_variables=['context', 'question'])
    return prompt


def create_qa_chain(prompt, llm, db):
    llm_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=db.as_retriever(search_kwargs={'k':3}, max_tokens_limit=1024),
        return_source_documents=False,
        chain_type_kwargs={'prompt':prompt}
    )
    return llm_chain

def read_vector_db(vector_db_path, model_emb):
    db = FAISS.load_local(vector_db_path, model_emb)
    return db