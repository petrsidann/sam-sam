import os
import requests
import json

# Fetch your hidden OpenRouter API key from the cloud environment
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("Error: Missing OpenRouter API Key!")
    exit(1)

# Configure the OpenRouter request using a 100% free model
url = "https://openrouter.ai"
headers = {
    "Authorization": f"Bearer {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}",
    "Content-Type": "application/json"
}

data = {
    "model": "qwen/qwen-2.5-coder-32b:free", # Runs completely free
    "messages": [
        {"role": "user", "content": "Generate one highly specific, low-competition micro-SaaS or digital product idea that can be built by an AI agent to make money. Provide the concept and a target audience. Keep it concise."}
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))
result = response.json()

try:
    ai_idea = result['choices'][0]['message']['content']
    
    # Save the idea automatically to a markdown file
    with open("ideas_log.md", "a") as f:
        f.write(f"\n\n### Automated Agent Update\n{ai_idea}")
    print("Successfully generated and saved a new idea!")
except Exception as e:
    print("Failed to parse AI response:", e)
    print("Raw response:", result)
