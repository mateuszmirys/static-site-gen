from textnode import TextType, TextNode

def main(text, text_type, url):
    print("Hello World!")
    new_text_node = TextNode(text, text_type, url)
    print(new_text_node)

main('smth', TextType.CODE, 'mirys.pl')
