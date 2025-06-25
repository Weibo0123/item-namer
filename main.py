import requests
import argparse

def generate_item_name(style: str) -> str:
    prompt = f"给我起一个{style}风格的物品名称，只给出物品名称即可，不需要任何其他东西"

    api_response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return api_response.json()["response"].strip()


def main():
    parser = argparse.ArgumentParser(description="物品命名器 - 使用本地 LLaMA3 模型")
    parser.add_argument('--style', type=str, default="魔幻", help="风格（如 魔幻、科幻、东方、蒸汽朋克）")
    parser.add_argument('--count', type=int, default=1, help="生成数量")
    args = parser.parse_args()

    print(f"\n🎨 正在生成 {args.count} 个『{args.style}』风格的物品名称...\n")
    for i in range(args.count):
        name = generate_item_name(args.style)
        print(f"{i + 1}. {name}")

if __name__ == "__main__":
    main()
