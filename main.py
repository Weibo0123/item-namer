import requests
import argparse

def generate_item_names(style: str, count: int) -> list[str]:
    prompt = (
        f"请帮我生成 {count} 个{style}风格的物品名称，"
        f"要求每个名称独立且富有创意，中文回答，"
        f"只列出物品名称，不要添加解释或其他文字，除了物品名称其他一律不要。"
    )

    api_response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    # 按行分割，去掉空行和多余符号
    raw_output = api_response.json()["response"]
    lines = raw_output.strip().splitlines()

    # 清洗行，例如去掉编号、引号
    cleaned = []
    for line in lines:
        line = line.strip()
        line = line.lstrip("0123456789.、- ")
        line = line.strip("“”\"'（）[]")
        if line:
            cleaned.append(line)
    return cleaned


def main():
    parser = argparse.ArgumentParser(description="物品命名器 - 使用本地 LLaMA3 模型")
    parser.add_argument('--style', type=str, default="魔幻", help="风格（如 魔幻、科幻、东方、蒸汽朋克）")
    parser.add_argument('--count', type=int, default=5, help="生成数量")
    args = parser.parse_args()

    print(f"\n🎨 正在生成 {args.count} 个『{args.style}』风格的物品名称...\n")
    names = generate_item_names(args.style, args.count)
    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")

if __name__ == "__main__":
    main()
