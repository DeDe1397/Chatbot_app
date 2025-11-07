Demo_Chatbot_app
PDFやCSVファイルを対象に、質問応答を行う生成AIチャットボット FastAPI + Streamlit + LangChain + OpenAI を活用したデモアプリケーションです。

## ２つの機能
⓵CSVチャット

CSVファイルをアップロードし、自然言語で要約・統計分析を依頼可能

![csv要約](https://raw.githubusercontent.com/DeDe1397/Chatbot_app/refs/heads/main/csv.avif)

➁PDF検索チャット（RAG）

PDFを読み込み、関連箇所を検索して回答を生成

![PDF要約](https://raw.githubusercontent.com/DeDe1397/Chatbot_app/refs/heads/main/pdf.avif)

## フロントエンド & バックエンド
StreamlitによるUI、FastAPIによるAPIサーバー
ベクトル検索
FAISSによる高速な類似検索

## Tech Stack
言語/環境: Python
ライブラリ: LangChain, OpenAI, FAISS, FastAPI, Streamlit
その他: dotenv (環境変数管理)

## 依存インストール
```bash
pip install -r requirements.txt
streamlit run app.py
uvicorn api:app --reload
```

## 環境変数（.env）
```bash
OPENAI_API_KEY=your_openai_api_key
```

## 追加機能検討事項
最大ファイルサイズ、対応拡張子、タイムアウト、PDF：OCR

## Qiita記事
https://qiita.com/c62323440/items/79c2bfb65c3adb757c36