import os
import shutil

from markdown_blocks import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks,
    markdown_to_html_node,
)


def copy_files_recursive(source: str = None, target: str = None, clean: bool = False):
    if not os.path.isdir(source):
        raise Exception("Source is not directory error")

    if clean:
        if os.path.isdir(target):
            shutil.rmtree(target)
            print(f"Cleaned target: ", target)

    if not os.path.isdir(target):
        os.mkdir(target)
        print("Created target: ", target)

    for file in os.listdir(source):
        source_path = os.path.join(source, file)
        target_path = os.path.join(target, file)
        if os.path.exists(source_path):
            if os.path.isdir(source_path):
                copy_files_recursive(source_path, target_path, False)
            else:
                shutil.copy(source_path, target_path)
                print("Copied: ", source_path, target_path)


def extract_title(markdown: str):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING and block.startswith("# "):
            return block.replace("#", "").strip()
    raise Exception("No h1 markdown found for title")


def generate_page(from_path, template_path, dest_path, basepath):
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path} with basepath {basepath}"
    )

    with open(from_path, "r") as file:
        from_path_content = file.read()

    with open(template_path, "r") as file:
        template_path_content = file.read()

    title = extract_title(from_path_content)
    html_content = markdown_to_html_node(from_path_content).to_html()

    filtered_content = (
        template_path_content.replace("{{ Title }}", title)
        .replace("{{ Content }}", html_content)
        .replace('href="/', 'href="' + basepath)
        .replace('src="/', 'src="' + basepath)
    )

    with open(dest_path, "a") as file:
        file.write(filtered_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.isdir(dest_dir_path):
        os.mkdir(dest_dir_path)
        print("Created target: ", dest_dir_path)

    for file in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, file)
        target_path = os.path.join(dest_dir_path, file)
        if os.path.exists(source_path):
            if os.path.isdir(source_path):
                generate_pages_recursive(
                    source_path, template_path, target_path, basepath
                )
            else:

                generate_page(
                    source_path,
                    template_path,
                    target_path.split(".")[0] + ".html",
                    basepath,
                )
