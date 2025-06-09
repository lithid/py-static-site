from typing import List, Self


class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: List[Self] = None,
        props: dict = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, node):
        return (
            node.tag == self.tag
            and node.value == self.value
            and node.children == self.children
            and node.props == self.props
        )

    def to_html(self):
        raise NotImplementedError("to_html must be implemented")

    def props_to_html(self) -> str:
        return " ".join(map(lambda x: f'{x[0]}="{x[1]}"', self.props.items()))
