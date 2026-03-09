import ast

class CodeParser:
    def __init__(self, code):
        self.code = code
        self.tree = ast.parse(code)

    def get_tree(self):
        return self.tree

    def get_nodes(self):
        nodes = []
        for node in ast.walk(self.tree):
            nodes.append(type(node).__name__)
        return nodes