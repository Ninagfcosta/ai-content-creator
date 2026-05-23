import os


def read_markdown_file(file_path):
    """Read a single markdown file and return its content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def load_knowledge_base(folder_path):
    """
    Load all markdown files from a folder.
    Returns a dictionary: {filename: content}
    """
    knowledge = {}

    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return knowledge

    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            full_path = os.path.join(folder_path, filename)
            content = read_markdown_file(full_path)
            knowledge[filename] = content
            print(f"Loaded: {filename}")

    return knowledge


def combine_documents(knowledge_dict):
    """Combine all documents into one text block for prompts."""
    combined = ""
    for filename, content in knowledge_dict.items():
        combined += f"\n\n--- {filename} ---\n\n"
        combined += content
    return combined


if __name__ == "__main__":
    primary = load_knowledge_base("knowledge_base/primary")
    secondary = load_knowledge_base("knowledge_base/secondary")
    print("\nPrimary files:", list(primary.keys()))
    print("Secondary files:", list(secondary.keys()))