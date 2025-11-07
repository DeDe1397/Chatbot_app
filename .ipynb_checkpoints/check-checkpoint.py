import pandas as pd
from ask_to_api import get_qa_chain

test_data = [
    {"question": "北海道の小学性の算数の平均値はいくら？", "expected": "55.0です。"},
    {"question": "北海道の小学性の国語の平均値はいくら？", "expected": "65.0です。"},
    {"question": "北海道の小学性の理科の平均値はいくら？", "expected": "56.0です。"},   
    {"question": "北海道の小学性の算数の標準偏差はいくら？", "expected": "25.3です。"},    
    {"question": "北海道の小学性の国語の標準偏差はいくら？", "expected": "22.5です。"},
    {"question": "北海道の小学性の理科の標準偏差はいくら？", "expected": "21.6です。"},    
    {"question": "青森の小学性の算数の平均値はいくら？", "expected": "57.0です。"},
    {"question": "青森の小学性の国語の平均値はいくら？", "expected": "59.0です。"},
    {"question": "青森の小学性の理科の平均値はいくら？", "expected": "67.0です。"},   
    {"question": "青森の小学性の算数の標準偏差はいくら？", "expected": "24.4です。"},    
    {"question": "青森の小学性の国語の標準偏差はいくら？", "expected": "21.0です。"},
    {"question": "青森の小学性の理科の標準偏差はいくら？", "expected": "20.4です。"},      
]

qa_chain = get_qa_chain()

results = []
for item in test_data:
    answer = qa_chain.run(item["question"])
    results.append({
        "question": item["question"],
        "expected": item["expected"],
        "answer": answer,
        "is_correct": item["expected"] in answer  
    })

df = pd.DataFrame(results)
accuracy = df["is_correct"].mean()
print(df)
print("正答率:", accuracy)
df.to_csv("rag_evaluation_results.csv", index=False)
