from pagegeneration import copystatic, generate_pages_recursive

def main():
    copystatic("static", "public")
    generate_pages_recursive("content", "template.html", "public")

main()