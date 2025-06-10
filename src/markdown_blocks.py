def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    return list(filter(lambda x: x != "", list(map(lambda x: x.strip("\n"), blocks))))
