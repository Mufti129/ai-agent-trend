import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_trend(data):
    prompt = f"""
    Analisa tren berikut:
    {data}

    Buat:
    1. Insight tren
    2. Peluang bisnis
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content


def generate_campaign(insight):
    prompt = f"""
    Dari insight ini:
    {insight}

    Buat:
    1. 5 ide konten TikTok
    2. Hook viral
    3. Caption + hashtag
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content
