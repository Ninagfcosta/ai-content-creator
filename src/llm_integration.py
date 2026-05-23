import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

def generate_content(prompt, max_tokens=1000):
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    try:
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=max_tokens,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    print("Testing API connection...")
    result = generate_content("Say hello from NovaTech Apps in one sentence.")
    if result:
        print("SUCCESS! API Response:")
        print(result)
    else:
        print("FAILED - Check your API key")
        