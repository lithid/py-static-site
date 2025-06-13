import sys
from utils import copy_files_recursive, generate_pages_recursive


def main(basepath):
    print("Using basepath: ", basepath)
    copy_files_recursive("static", "docs", True)
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    basepath = "/"
    if len(sys.argv) == 2:
        basepath = sys.argv[1]
    main(basepath)
