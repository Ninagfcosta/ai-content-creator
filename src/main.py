import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.document_processor import load_knowledge_base
from src.prompt_templates import create_social_media_prompt
from src.llm_integration import generate_content

def main():
    print("Loading knowledge bases...")
    primary = load_knowledge_base("knowledge_base/primary")
    secondary = load_knowledge_base("knowledge_base/secondary")

    brand_context = "\n".join(primary.values())
    market_context = "\n".join(secondary.values())

    prompt = create_social_media_prompt(
        brand_context=brand_context,
        market_context=market_context,
        content_type="Instagram post"
    )

    print("Generating content...")
    result = generate_content(prompt)

    print("\n--- GENERATED CONTENT ---")
    print(result)

if __name__ == "__main__":
    main()
    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
    