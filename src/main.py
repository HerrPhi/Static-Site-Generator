from textnode import TextNode, TextType

from markdown_to_html import markdown_to_html_node

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)



if __name__ == "__main__":
    main()