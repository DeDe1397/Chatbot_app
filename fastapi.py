from fastapi import FastAPI                 
from pydantic import BaseModel         

qa_chain = None  

from ask_to_api import get_qa_chain
app = FastAPI(title="RAG QA API")      

class Question(BaseModel):            
    query: str                       

def load_qa_chain():
    global qa_chain
    if qa_chain is None:
        from pdf_load_LLM_ask import qa_chain as loaded_chain
        qa_chain = loaded_chain
    return qa_chain

@app.post("/ask")                      
async def ask(question: Question):      
    qa_chain = get_qa_chain()
    answer = qa_chain.run(question.query)
    return {"answer": answer}
