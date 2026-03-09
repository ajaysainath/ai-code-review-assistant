import ast

class RulesEngine(ast.NodeVisitor):

    def __init__(self):
        self.suggestions = []
        self.assigned = set()
        self.used = set()

    # Detect inefficient loops
    def visit_For(self, node):

        if isinstance(node.iter, ast.Call):
            if isinstance(node.iter.func, ast.Name) and node.iter.func.id == "range":
                if node.iter.args:
                    arg = node.iter.args[0]

                    if isinstance(arg, ast.Call) and getattr(arg.func, "id", "") == "len":

                        self.suggestions.append({
                            "issue": "Inefficient loop",
                            "suggestion": "Use Pythonic iteration instead of range(len()).",
                            "example": "for item in arr:\n    print(item)"
                        })

        self.generic_visit(node)

    # Track assigned variables
    def visit_Assign(self, node):

        for target in node.targets:
            if isinstance(target, ast.Name):
                self.assigned.add(target.id)

        self.generic_visit(node)

    # Track used variables
    def visit_Name(self, node):

        if isinstance(node.ctx, ast.Load):
            self.used.add(node.id)

        self.generic_visit(node)

    # Detect unused variables
    def check_unused_variables(self):

        unused = self.assigned - self.used

        for var in unused:
            self.suggestions.append({
                "issue": "Unused variable",
                "suggestion": f"Variable '{var}' is defined but never used."
            })

    # Detect bad variable names
    def check_bad_variable_names(self):

        for var in self.assigned:

            if len(var) <= 1:
                self.suggestions.append({
                    "issue": "Bad variable naming",
                    "suggestion": f"Variable '{var}' is too short. Use a descriptive name."
                })

    # Main analysis function
    def analyze(self, tree):

        self.visit(tree)

        self.check_unused_variables()

        self.check_bad_variable_names()

        issues_count = len(self.suggestions)

        score = max(10 - issues_count, 0)

        return {
            "quality_score": score,
            "issues_found": issues_count,
            "suggestions": self.suggestions
        }
    
    def visit_For(self, node):

        # Detect inefficient loop
            if isinstance(node.iter, ast.Call):
                if isinstance(node.iter.func, ast.Name) and node.iter.func.id == "range":
                    if node.iter.args:
                        arg = node.iter.args[0]

                        if isinstance(arg, ast.Call) and getattr(arg.func, "id", "") == "len":

                            self.suggestions.append({
                                "issue": "Inefficient loop",
                                "suggestion": "Use Pythonic iteration instead of range(len()).",
                                "example": "for item in arr:\n    print(item)"
                            })

            # Detect nested loops
            for child in ast.walk(node):
                if isinstance(child, ast.For) and child is not node:
                    self.suggestions.append({
                        "issue": "Nested loop detected",
                        "suggestion": "Nested loops may cause performance issues. Consider optimizing the algorithm."
                    })
                    break

            self.generic_visit(node)