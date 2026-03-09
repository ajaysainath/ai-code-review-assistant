from fastapi import UploadFile, File
from fastapi import FastAPI
from pydantic import BaseModel
from analyzer.code_parser import CodeParser
from analyzer.rules_engine import RulesEngine
from ai_suggestions.suggestion_model import generate_ai_suggestions
from analyzer.project_analyzer import analyze_project

app = FastAPI()


# Request model
class CodeRequest(BaseModel):
    code: str


@app.get("/")
def health_check():
    return {"status": "AI Code Review Assistant running"}


@app.post("/review")
def review_code(request: CodeRequest):
    try:
        code = request.code

        # Parse code into AST
        parser = CodeParser(code)
        tree = parser.get_tree()

        # Run rule engine
        engine = RulesEngine()
        analysis_result = engine.analyze(tree)

        # AI suggestions
        ai_result = generate_ai_suggestions(code)

        return {
            "quality_score": analysis_result["quality_score"],
            "issues_found": analysis_result["issues_found"],
            "rule_based_suggestions": analysis_result["suggestions"],
            "ai_analysis": ai_result
        }

    except Exception as e:
        return {"error": str(e)}
def check_bad_variable_names(self):

    for var in self.assigned:

        if len(var) <= 1:

            self.suggestions.append({
                "issue": "Bad variable naming",
                "suggestion": f"Variable '{var}' is too short. Use a descriptive name."
            })

@app.post("/review-file")
async def review_file(file: UploadFile = File(...)):
    try:

        # read uploaded file
        contents = await file.read()

        # convert bytes → string
        code = contents.decode("utf-8")

        # parse code
        parser = CodeParser(code)
        tree = parser.get_tree()

        # run analyzer
        engine = RulesEngine()
        analysis_result = engine.analyze(tree)

        # AI suggestions
        ai_result = generate_ai_suggestions(code)

        return {
            "filename": file.filename,
            "quality_score": analysis_result["quality_score"],
            "issues_found": analysis_result["issues_found"],
            "rule_based_suggestions": analysis_result["suggestions"],
            "ai_analysis": ai_result
        }

    except Exception as e:
        return {"error": str(e)}

@app.post("/review-project")
def review_project(folder_path: str):

    result = analyze_project(folder_path)

    return result