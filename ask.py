import os
from dotenv import load_dotenv

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

_qa_chain = None

def get_qa_chain():
    global _qa_chain

    if _qa_chain is None:
        load_dotenv()
        if "OPENAI_API_KEY" not in os.environ:
            raise ValueError("OPENAI_API_KEY が環境変数として設定されていません。 .env を確認してください。")
        embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002")
        vectorstore = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)
        _qa_chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
            retriever=vectorstore.as_retriever(k=3)
        )
    return _qa_chain

if __name__ == "__main__":
    qa_chain = get_qa_chain()

    while True:
        query = input("質問をどうぞ（exitで終了）: ")
        if query.lower() == "exit":
            break

        answer = qa_chain.run(query)
        print("\n 回答:")
        print(answer)
        print("--------------------------------------------------")
