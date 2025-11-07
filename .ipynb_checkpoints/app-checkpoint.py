import streamlit as st   
import pandas as pd      
import requests          
from dotenv import load_dotenv  
from openai import OpenAI       
import os

load_dotenv()            
client = OpenAI()        

# FastAPIのURL（RAGで検索する /ask エンドポイント）
RAG_API_URL = "http://127.0.0.1:8000/ask"


st.set_page_config(page_title="AIデータアシスタント", page_icon="🤖", layout="wide")
st.title("🤖 AIデータアシスタント")
st.markdown("CSVの要約チャット ＆ PDF検索チャット（RAG対応）")

if "messages" not in st.session_state:
    st.session_state["messages"] = []  

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

mode = st.radio(
    "モードを選んでください👇",
    ("CSV要約チャット", "PDF検索チャット（RAG）")
)

if mode == "CSV要約チャット":

    uploaded_file = st.file_uploader("📂 CSVファイルをアップロードしてください", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        summary_stats = df.describe().to_dict()
        sample_rows = df.head(3).to_dict(orient="records")
        if prompt := st.chat_input("このデータについて質問してください（例：要約して / 変化を教えて）"):
            st.session_state["messages"].append({"role": "user", "content": prompt})
            st.chat_message("user").markdown(prompt)
            full_prompt = f"""
            あなたは優秀なデータアナリストです。
            次のCSVデータに基づいて質問に答えてください。
            ▼統計量（describe）
            {summary_stats}
            ▼サンプルデータ（先頭3行）
            {sample_rows}
            ▼ユーザーからの質問
            {prompt}
            """

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": full_prompt}],
                max_tokens=500
            )
            answer = response.choices[0].message.content
            st.session_state["messages"].append({"role": "assistant", "content": answer})
            st.chat_message("assistant").markdown(answer)
else:
    if prompt := st.chat_input("PDFの内容について質問してください（例：北海道の算数の平均値は？）"):
        st.session_state["messages"].append({"role": "user", "content": prompt})
        st.chat_message("user").markdown(prompt)
        try:
            response = requests.post(RAG_API_URL, json={"query": prompt})
            answer = response.json().get("answer", "エラー: 回答が取得できませんでした")
        except Exception as e:
            answer = f"サーバーに接続できませんでした: {e}"
        st.session_state["messages"].append({"role": "assistant", "content": answer})
        st.chat_message("assistant").markdown(answer)
