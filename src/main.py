import os
import sys

from textnode import TextNode, TextType
from copystatic import copystatic
from gencontent import generate_page, generate_pages_recursive

from markdown_to_html import markdown_to_html_node

def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    source_path = os.path.join(".","static")
    destination_path = os.path.join(".","docs")

    if os.path.exists(source_path):
        copystatic(source_path, destination_path)

    from_dir = "content"
    template_path = "template.html"
    dest_dir = "docs"
    if os.path.exists(from_dir) and os.path.exists(template_path):
        generate_pages_recursive(from_dir, template_path, dest_dir, basepath)



if __name__ == "__main__":
    main()