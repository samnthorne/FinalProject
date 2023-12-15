import json
import sys

def count_words_in_markdown_cells():
    with open(notebook_path, 'r', encoding='utf-8') as file:
        notebook = json.load(file)

    word_count = 0
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            text = ''.join(cell['source'])
            word_count += len(text.split())

    return word_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_md_words.py [path_to_notebook.ipynb]")
        sys.exit(1)

    notebook_path = sys.argv[1]
    count = count_words_in_markdown_cells(notebook_path)
    print(f"Total word count in markdown cells: {count}")
