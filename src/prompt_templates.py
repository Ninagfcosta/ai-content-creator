def blog_post_template(primary_context, secondary_context, topic):
    """Template 1: Brand-aligned blog post."""
    return f"""You are a content writer for NovaTech Apps, a tech company 
with a specific brand voice and product lineup.

COMPANY KNOWLEDGE BASE:
{primary_context}

MARKET RESEARCH:
{secondary_context}

TASK:
Write a 300-400 word blog post about: {topic}

REQUIREMENTS:
- Use NovaTech's brand voice (friendly, innovative, jargon-free)
- Reference specific NovaTech products where relevant
- Include at least one market insight from the research
- End with a clear call-to-action related to NovaTech products
- Do NOT sound like a generic AI article
- Use specific product names, numbers, and brand language

Write the blog post now:"""


def social_media_template(primary_context, platform, topic):
    """Template 2: Social media post for specific platforms."""
    char_limits = {
        "twitter": "280 characters",
        "linkedin": "1300 characters",
        "instagram": "2200 characters"
    }
    limit = char_limits.get(platform.lower(), "300 characters")

    return f"""You are the social media manager for NovaTech Apps.

COMPANY KNOWLEDGE BASE:
{primary_context}

TASK:
Write a {platform} post about: {topic}
Maximum length: {limit}

REQUIREMENTS:
- Match NovaTech's brand voice exactly
- Reference specific products or features when relevant
- Include relevant hashtags for {platform}
- Sound human, not robotic
- Be engaging and unique

Write the {platform} post now:"""


def hybrid_content_template(
    primary_context, secondary_context, content_type, topic
):
    """Template 3: Hybrid content using both knowledge bases."""
    return f"""You are a senior content strategist for NovaTech Apps.

COMPANY KNOWLEDGE BASE:
{primary_context}

MARKET INTELLIGENCE:
{secondary_context}

TASK:
Create a {content_type} about: {topic}

STRATEGY:
- Position NovaTech against competitors using market research
- Use specific data points and statistics
- Align all messaging with NovaTech's brand voice
- Highlight NovaTech's unique differentiation
- Include a unique angle that generic AI content would miss

Create the {content_type} now:"""