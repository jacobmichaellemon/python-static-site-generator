from pagegeneration import copystatic, generate_page

def main():
    copystatic("static", "public")
    generate_page("content/index.md", "template.html", "public")
    generate_page("content/blog/glorfindel/index.md", "template.html", "public/blog/glorfindel")
    generate_page("content/blog/tom/index.md", "template.html", "public/blog/tom")
    generate_page("content/blog/majesty/index.md", "template.html", "public/blog/majesty")
    generate_page("content/contact/index.md", "template.html", "public/contact")

main()