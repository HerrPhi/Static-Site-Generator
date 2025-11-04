from markdown_to_html import markdown_to_html_node

import os, shutil

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            line = line.strip(" ")
            return line[2:]
    raise Exception("no h1 header")


def generate_page(from_path, template_path, dest_path, basepath):

    print(f"generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as markdown_file:
        from_path_markdown = markdown_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    HTML_node = markdown_to_html_node(from_path_markdown)
    HTML_string = HTML_node.to_html()

    title = extract_title(from_path_markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", HTML_string)

    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as dest_file:
        dest_file.write(template)
    

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):

    os.makedirs(dest_dir_path, exist_ok=True)
    
    content = os.listdir(dir_path_content)
    for entry in content:
        entry_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(entry_path):
            if entry_path.endswith(".md"):
                entry_html = f"{entry[:-3]}.html"
                dest_path = os.path.join(dest_dir_path, entry_html)
                generate_page(entry_path, template_path, dest_path, basepath)
            else:
                shutil.copy(entry_path, dest_dir_path)
        else:
            new_content_path = entry_path
            new_dest_dir_path = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(new_content_path, template_path, new_dest_dir_path, basepath)

