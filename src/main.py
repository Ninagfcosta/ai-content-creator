import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from content_pipeline import ContentPipeline


def print_banner():
    print("=" * 60)
    print("   NOVATECH APPS — AI CONTENT CREATOR")
    print("   Powered by OpenAI GPT-4")
    print("=" * 60)
    print()


def show_menu():
    print("\nWhat would you like to create?")
    print("1. Blog Post")
    print("2. LinkedIn Post")
    print("3. Twitter Post")
    print("4. Hybrid Content")
    print("5. Exit")
    return input("\nEnter your choice (1-5): ").strip()


def get_topic():
    return input("Enter the topic: ").strip()


def main():
    print_banner()
    print("Loading NovaTech knowledge bases...")

    try:
        pipeline = ContentPipeline()
        print("System ready!\n")
    except Exception as e:
        print(f"Error loading pipeline: {e}")
        return

    while True:
        choice = show_menu()

        if choice == "1":
            topic = get_topic()
            content = pipeline.create_blog_post(topic)
            if content:
                print("\n" + "=" * 40)
                print("GENERATED BLOG POST:")
                print("=" * 40)
                print(content)
                pipeline.save_content(
                    content,
                    f"blog_{topic[:20].replace(' ', '_')}.md"
                )

        elif choice == "2":
            topic = get_topic()
            content = pipeline.create_social_post("linkedin", topic)
            if content:
                print("\n" + "=" * 40)
                print("GENERATED LINKEDIN POST:")
                print("=" * 40)
                print(content)
                pipeline.save_content(
                    content,
                    f"linkedin_{topic[:20].replace(' ', '_')}.md"
                )

        elif choice == "3":
            topic = get_topic()
            content = pipeline.create_social_post("twitter", topic)
            if content:
                print("\n" + "=" * 40)
                print("GENERATED TWITTER POST:")
                print("=" * 40)
                print(content)
                pipeline.save_content(
                    content,
                    f"twitter_{topic[:20].replace(' ', '_')}.md"
                )

        elif choice == "4":
            topic = get_topic()
            content_type = input(
                "Content type (e.g. 'thought leadership article'): "
            ).strip()
            content = pipeline.create_hybrid_content(
                content_type, topic
            )
            if content:
                print("\n" + "=" * 40)
                print(f"GENERATED {content_type.upper()}:")
                print("=" * 40)
                print(content)
                pipeline.save_content(
                    content,
                    f"hybrid_{topic[:20].replace(' ', '_')}.md"
                )

        elif choice == "5":
            print("\nThank you for using NovaTech AI Content Creator!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()