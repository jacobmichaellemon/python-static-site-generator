from pagegeneration import copystatic, generate_page
def main():
    copystatic("static", "public")
    generate_page("content/index.md", "template.html", "public")

main()