import os
from analyzer.code_parser import CodeParser
from analyzer.rules_engine import RulesEngine


def analyze_project(folder_path):

    results = []
    total_score = 0
    total_issues = 0
    file_count = 0

    for root, dirs, files in os.walk(folder_path):

        for file in files:

            if file.endswith(".py"):

                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8") as f:
                    code = f.read()

                parser = CodeParser(code)
                tree = parser.get_tree()

                engine = RulesEngine()
                analysis = engine.analyze(tree)

                results.append({
                    "file": file,
                    "quality_score": analysis["quality_score"],
                    "issues_found": analysis["issues_found"]
                })

                total_score += analysis["quality_score"]
                total_issues += analysis["issues_found"]
                file_count += 1

    avg_score = total_score / file_count if file_count else 0

    return {
        "files_analyzed": file_count,
        "average_quality_score": round(avg_score, 2),
        "total_issues": total_issues,
        "file_reports": results
    }