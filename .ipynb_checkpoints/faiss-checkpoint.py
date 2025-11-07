import os
from dotenv import load_dotenv  

from langchain_community.document_loaders import PyPDFLoader  
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter  
from langchain_community.embeddings import OpenAIEmbeddings  
from langchain_community.vectorstores import FAISS  #

# .env には以下のように書いておく：
# OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
load_dotenv()

# PDFファイルがすべて入っているフォルダdocsのパスを指定
directory_path = "docs" 
loader = DirectoryLoader(
    directory_path,
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)
documents = loader.load() 
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,        
    chunk_overlap=50       
)
docs = text_splitter.split_documents(documents)
embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002")
vectorstore = FAISS.from_documents(docs, embedding_model)
vectorstore.save_local("faiss_index")  