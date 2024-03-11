from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import FAISS
from config import get_config
from utils import load_llm, create_prompt, create_qa_chain, read_vector_db

config = get_config()

model_file = config.model_llm
vector_db_path = config.vector_db_path
model_emb = GPT4AllEmbeddings(model_file=config.model_emb)
question = config.question


db = read_vector_db(vector_db_path, model_emb)
llm = load_llm(model_file)

template = """<|im_start|>system\nSử dụng thông tin sau đây để trả lời câu hỏi. Nếu bạn không biết câu trả lời, hãy nói không biết, đừng cố tạo ra câu trả lời\n
    {context}<|im_end|>\n<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant"""
prompt = create_prompt(template)

llm_chain = create_qa_chain(prompt, llm, db)

response = llm_chain.invoke({'query':question})

print(response)