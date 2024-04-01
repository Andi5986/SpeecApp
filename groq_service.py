from groq import Groq
from config import Config

client = Groq(api_key=Config.GROQ_API_KEY)


def execute(prompt):
    completion = client.chat.completions.create(
        model=Config.GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=Config.GROQ_TEMPERATURE,
        max_tokens=Config.GROQ_MAX_TOKENS,
        top_p=Config.GROQ_TOP_P,
        stream=Config.GROQ_STREAM,
        stop=Config.GROQ_STOP,
    )

    response = ''
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""

    return response
