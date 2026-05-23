import os

def load_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def load_knowledge_base(folder_path):
    documents = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            full_path = os.path.join(folder_path, filename)
            documents[filename] = load_document(full_path)
    return documents
