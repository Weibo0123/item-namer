import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": "给我起个魔幻风格的物品名称，用中文回答我这个问题，所有的都是中文",
        "stream": False
    }
)
print(response.json()["response"])
