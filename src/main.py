import os

from textnode import TextNode, TextType
from copystatic import copystatic
from gencontent import generate_page, generate_pages_recursive

from markdown_to_html import markdown_to_html_node

def main():
    
    source_path = os.path.join(".","static")
    destination_path = os.path.join(".","public")

    if os.path.exists(source_path):
        copystatic(source_path, destination_path)

    #from_path = "content/index.md"
    #template_path = "template.html"
    #dest_path = "public/index.html"
    #if os.path.exists(from_path) and os.path.exists(template_path):
    #    generate_page(from_path, template_path, dest_path)

    from_dir = "content"
    template_path = "template.html"
    dest_dir = "public"
    if os.path.exists(from_dir) and os.path.exists(template_path):
        generate_pages_recursive(from_dir, template_path, dest_dir)



if __name__ == "__main__":
    main()