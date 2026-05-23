import openai
import os
from dotenv import load_dotenv

load_dotenv()


def generate_content(prompt, max_tokens=1000):
    """
    Generate content using OpenAI API.
    """
    client = openai.OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=max_tokens,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    except openai.AuthenticationError as e:
        print(f"Authentication Error: {e}")
        return None

    except openai.RateLimitError as e:
        print(f"Rate Limit Error: {e}")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    print("=" * 50)
    print("NOVATECH APPS - AI Content Creator")
    print("Testing OpenAI API connection...")
    print("=" * 50)

    result = generate_content(
        "Say hello from NovaTech Apps in one sentence."
    )

    if result:
        print("\nSUCCESS! API Response:")
        print("-" * 40)
        print(result)
        print("-" * 40)
    else:
        print("FAILED - Check your API key")