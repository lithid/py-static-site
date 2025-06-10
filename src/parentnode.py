from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError(f"{__name__} tag is required")

        if self.children == None:
            raise ValueError(f"{__name__} children is required")

        props = ""
        if self.props != None:
            props = " " + self.props_to_html()

        return f"<{self.tag}{props}>{"".join(map(lambda x: x.to_html(), self.children))}</{self.tag}>"
