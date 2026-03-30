import os
from openai import OpenAI

# Koneksi ke OpenRouter (GRATIS)
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def analyze_trend(data):
    try:
        prompt = f"""
        Analisa tren berikut:
        {data}

        Buat:
        1. Insight tren
        2. Peluang bisnis
        """

        res = client.chat.completions.create(
            #model="mistralai/mistral-7b-instruct",
            model="openchat/openchat-7b",
            messages=[{"role": "user", "content": prompt}]
        )

        return res.choices[0].message.content

    except Exception as e:
        return f"Error saat analisa tren: {str(e)}"


def generate_campaign(insight):
    try:
        prompt = f"""
        Dari insight ini:
        {insight}

        Buat:
        1. 5 ide konten TikTok
        2. Hook viral
        3. Caption + hashtag
        """

        res = client.chat.completions.create(
            #model="mistralai/mistral-7b-instruct",
            model="openchat/openchat-7b",
            messages=[{"role": "user", "content": prompt}]
        )

        return res.choices[0].message.content

    except Exception as e:
        return f"Error saat generate campaign: {str(e)}"
