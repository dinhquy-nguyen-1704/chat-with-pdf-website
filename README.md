# chat-with-pdf-website
## 1. Introduction
## 2. Getting Started
```
git clone https://github.com/dinhquy-nguyen-1704/chat-with-pdf-website.git
cd chat-with-pdf-website
```
```
conda create --name chat-with-pdf-website python=3.10
conda activate chat-with-pdf-website
```
```
pip install -r requirements.txt
```
## 3. Inference
### 3.1 chat_with_pdf
First, change to the **chat_with_pdf** directory and create new folder **models**.
```
cd chat_with_pdf
mkdir models
```
Then, download models (**LLM** and **embedding model**) you want to use. In my source code, the default LLM is [vinallama-2.7b-chat_q5_0.gguf](vinallama-2.7b-chat_q5_0.gguf) and the default embedding model is [all-MiniLM-L6-v2-f16.gguf](https://huggingface.co/caliex/all-MiniLM-L6-v2-f16.gguf/tree/main). You should organize the folder structure as follows:

- 📁 chat-with-pdf-website
  - 📁 chat_with_pdf
    - 📂 data
      - 📄 your_file.pdf
    - 📁 models
      - all-MiniLM-L6-v2-f16.gguf
      - vinallama-2.7b-chat_q5_0.gguf
    - 📁 vectorstores
    - 🐍 config.py
    - 🐍 create_vector_db.py
    - 🐍 qa_bot.py
    - 🐍 utils.py
  - 📁 chat_with_website
    - 🐍 utils.py
    - 🐍 app.py
  - 📄 README.md
  - 📄 requirements.txt

> Delete 2 files **index.faiss** and **index.pkl** in **vectorstores** if you want to use **your_file.pdf**.

After that, run file create_vector_db.py
```
python create_vector_db.py
```
When the above command is completed, two files named **index.faiss** and **index.pkl** in will appear in the **vectorstores**.

Now, you can use chatbot to ask questions about the information in the **your_file.pdf** file in the command line environment.
```
python qa_bot.py --question "your_question"
```

### 3.2 chat_with_website
First, change to the **chat_with_website** directory
```
cd chat_with_website
```
Next, replace the OpenAI API key in the **app.py** file.
```python
import os
os.environ["OPENAI_API_KEY"] = "sk-..."
api_key = os.getenv("OPENAI_API_KEY")
```
Now, you can run the **app.py** file and a Streamlit chatbot interface will appear.
```
python -m streamlit run app.py
```
You can paste a link to any website and ask for information related to that website.
<p align="center">
  <img width="800" alt="Streamlit GUI" src="https://github.com/dinhquy-nguyen-1704/chat-with-pdf-website/assets/127675330/22917f92-bca7-44dc-89e1-4c50ba44adfe">
</p>
<p align="center">
  <em>Streamlit GUI</em>
</p>
