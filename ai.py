import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

PRIMARY_MODEL = "meta-llama/llama-3.3-70b-instruct:free"
FALLBACK_MODEL = "meta-llama/llama-3-8b-instruct:free"

def call_ai(prompt):
    try:
        res = client.chat.completions.create(
            model=PRIMARY_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content
    except Exception as e:
        print("Primary model gagal, pakai fallback...")
        res = client.chat.completions.create(
            model=FALLBACK_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content


def analyze_trend(data):
    prompt = f"""
    Analisa tren berikut:
    {data}

    Buat:
    1. Insight tren
    2. Peluang bisnis
    """
    return call_ai(prompt)


def generate_campaign(insight):
    prompt = f"""
    Dari insight ini:
    {insight}

    Buat:
    1. 5 ide konten TikTok
    2. Hook viral
    3. Caption + hashtag
    """
    return call_ai(prompt)
