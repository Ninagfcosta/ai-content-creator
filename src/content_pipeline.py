import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from document_processor import load_knowledge_base, combine_documents
from prompt_templates import (
    blog_post_template,
    social_media_template,
    hybrid_content_template
)
from llm_integration import generate_content


class ContentPipeline:
    """
    Orchestrates the full content creation pipeline.
    Document -> Brief -> Publish
    """

    def __init__(self):
        self.primary_docs = {}
        self.secondary_docs = {}
        self._load_knowledge_bases()

    def _load_knowledge_bases(self):
        """Stage 1 - Document: Load all knowledge base files."""
        print("=== Loading Knowledge Bases ===")

        # Get the project root path
        src_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(src_dir)

        primary_path = os.path.join(root_dir, "knowledge_base", "primary")
        secondary_path = os.path.join(root_dir, "knowledge_base", "secondary")

        self.primary_docs = load_knowledge_base(primary_path)
        self.secondary_docs = load_knowledge_base(secondary_path)

        print(f"Primary KB: {len(self.primary_docs)} files loaded")
        print(f"Secondary KB: {len(self.secondary_docs)} files loaded")
        print()

    def get_primary_context(self):
        """Return primary docs as text."""
        return combine_documents(self.primary_docs)

    def get_secondary_context(self):
        """Return secondary docs as text."""
        return combine_documents(self.secondary_docs)

    def create_blog_post(self, topic):
        """Generate a brand-aligned blog post."""
        print(f"Creating blog post about: {topic}")
        prompt = blog_post_template(
            primary_context=self.get_primary_context(),
            secondary_context=self.get_secondary_context(),
            topic=topic
        )
        return generate_content(prompt, max_tokens=800)

    def create_social_post(self, platform, topic):
        """Generate a social media post."""
        print(f"Creating {platform} post about: {topic}")
        prompt = social_media_template(
            primary_context=self.get_primary_context(),
            platform=platform,
            topic=topic
        )
        return generate_content(prompt, max_tokens=400)

    def create_hybrid_content(self, content_type, topic):
        """Generate advanced hybrid content."""
        print(f"Creating {content_type} about: {topic}")
        prompt = hybrid_content_template(
            primary_context=self.get_primary_context(),
            secondary_context=self.get_secondary_context(),
            content_type=content_type,
            topic=topic
        )
        return generate_content(prompt, max_tokens=1000)

    def save_content(self, content, filename):
        """Save generated content to file."""
        src_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(src_dir)
        output_dir = os.path.join(root_dir, "generated_content")
        os.makedirs(output_dir, exist_ok=True)

        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Content saved to: {filepath}")
        return filepath