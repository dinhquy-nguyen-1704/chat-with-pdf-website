import argparse

def get_config():

    parser = argparse.ArgumentParser()

    parser.add_argument('--model_llm', type=str, default='models/vinallama-2.7b-chat_q5_0.gguf')
    parser.add_argument('--model_emb', type=str, default='models/all-MiniLM-L6-v2-f16.gguf')
    parser.add_argument('--vector_db_path', type=str, default='vectorstores')
    parser.add_argument('--question', type=str, default=None)  

    args = parser.parse_args()

    return args