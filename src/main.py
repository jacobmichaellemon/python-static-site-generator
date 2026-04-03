from pagegeneration import copystatic, generate_pages_recursive
import sys

def main():

    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    copystatic("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()