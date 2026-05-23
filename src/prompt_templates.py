def create_social_media_prompt(brand_context, market_context, content_type):
    return f"""
You are a content creator for NovaTech Apps.

BRAND GUIDELINES:
{brand_context}

MARKET TRENDS:
{market_context}

TASK:
Create a {content_type} for NovaTech Apps.
- Use the brand voice described above
- Reference current market trends
- Make it unique and engaging
- Do NOT use generic AI language

OUTPUT:
Write only the final content, ready to publish.
"""
