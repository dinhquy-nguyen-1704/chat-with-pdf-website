API_KEY = "sk-..."

from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import YoutubeLoader

text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50)
loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=tcqEUSNCn8I", add_video_info=True)
splits = loader.load_and_split(text_splitter)

emb = OpenAIEmbeddings(openai_api_key=API_KEY)
vectorstore = Chroma.from_documents(documents=splits, embedding=emb)

import gradio as gr
from openai import OpenAI

llm = OpenAI(api_key=API_KEY)

RAG_PROMPT = """Nhiệm vụ của bạn là trả lời câu hỏi của người dùng dựa trên dữ liệu được cho.
Nếu dữ liệu được cho không liên quan đến câu hỏi, vui lòng trả lời "Tôi không biết"
---
Dữ liệu: {context}
---
Câu hỏi: {question}
---
Trả lời:"""

def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    docs = vectorstore.similarity_search(message)
    context = docs[0].page_content
    history_openai_format.append({"role": "user", "content": RAG_PROMPT.format(context=context, question=message)})

    response = llm.chat.completions.create(model='gpt-3.5-turbo',
      messages= history_openai_format,
      temperature=1.0,
      stream=True)

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
              partial_message = partial_message + chunk.choices[0].delta.content
              yield partial_message


gr.ChatInterface(predict).launch()