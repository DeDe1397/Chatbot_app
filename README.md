# Demo_Chatbot_app

PDFやCSVファイルを対象に、質問応答を行う生成AIチャットボット
FastAPI + Streamlit + LangChain + OpenAI を活用したデモアプリケーションです。

## ２つの機能
⓵CSVチャット

CSVファイルをアップロードし、自然言語で要約・統計分析を依頼可能

➁PDF検索チャット（RAG）

PDFを読み込み、関連箇所を検索して回答を生成

## フロントエンド & バックエンド

StreamlitによるUI、FastAPIによるAPIサーバー

ベクトル検索

FAISSによる高速な類似検索

## Tech Stack

言語/環境: Python

ライブラリ: LangChain, OpenAI, FAISS, FastAPI, Streamlit

その他: dotenv (環境変数管理)
