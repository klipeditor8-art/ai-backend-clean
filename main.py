from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

# Postavi tvoj OpenAI API ključ
import os
openai.api_key = os.getenv("OPENAI_API_KEY")  # bolje sigurnosno rješenje

app = FastAPI(title="AI Build Log Analyzer")

# Model podataka koji očekujemo
class LogInput(BaseModel):
    logs: str

# Endpoint koji prima logove
@app.post("/analyze_logs")
async def analyze_logs(input: LogInput):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI debugging assistant."},
            {"role": "user", "content": f"Analyze these build logs and give suggestions:\n{input.logs}"}
        ],
        max_tokens=500
    )
    return {"analysis": response.choices[0].message.content}
