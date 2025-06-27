import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("MODEL_NAME", "gpt-4-turbo")

def analyze_metrics(metrics: dict) -> str:
    prompt = f"""
    You are a backend debugging assistant.
    Given these metrics, summarize the current health and recommend next steps:

    {metrics}
    """

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert in backend diagnostics."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message["content"]
