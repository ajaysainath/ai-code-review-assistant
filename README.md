**AI Code Review Assistant**

# AI Code Review Assistant

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![License](https://img.shields.io/badge/License-MIT-yellow)
![AI Code Review Assistant](assets/banner.png)

An AI-powered developer tool that analyzes Python code and suggests improvements related to code quality, performance, and best practices.

The system performs static code analysis using Python’s Abstract Syntax Tree (AST) and provides automated suggestions. It also includes a web interface and generates downloadable code review reports.

**Features**

Code snippet analysis
Python file analysis
Project folder analysis
Code quality scoring
Detection of inefficient loops
Detection of unused variables
Detection of poor variable naming
Detection of nested loops (performance issues)
AI generated improvement suggestions
Downloadable PDF code review report
Download improved code as .py file
Project health dashboard with charts

**Project Architecture**

The project uses a frontend + backend architecture.

            User
            ↓
     Streamlit UI (Frontend)
            ↓
         HTTP Request
            ↓
      FastAPI API (Backend)
            ↓
     Code Analyzer Engine
            ↓
     AST Static Analysis + AI Suggestions
            ↓
    Results returned to UI


**Project Structure**


ai-code-review-assistant/

analyzer/
    code_parser.py
    rules_engine.py
    project_analyzer.py

ai_suggestions/
    suggestion_model.py

api/
    app.py

reports/
    generate_report.py

ui/
    app1.py

requirements.txt
README.md

**Technologies Used**

    Python
    FastAPI
    Streamlit
    AST (Abstract Syntax Tree)
    Pandas
    ReportLab
    Requests

**How It Works**
The system follows these steps:

1.User provides Python code, a file, or a project folder.
2.FastAPI receives the request.
3.The code is parsed using Python AST.
4.The rules engine detects issues such as:
    inefficient loops
    unused variables
    bad variable naming
    nested loops
5.A code quality score is generated.
6.AI suggestions provide improved code.
7.Results are displayed in the Streamlit UI.

**Installation**
Clone the repository:

git clone https://github.com/yourusername/ai-code-review-assistant.git
cd ai-code-review-assistant

Install dependencies:

pip install -r requirements.txt

**Running the Backend**
Start the FastAPI server:

python -m uvicorn api.app:app --reload --port 8001

Open API docs:

http://127.0.0.1:8001/docs

**Running the Web Interface**
Start the Streamlit application:

python -m streamlit run ui/app1.py

Open in browser:

http://localhost:8501

**Example Output**

Code Quality Score
Issues Detected
Improvement Suggestions
AI Refactored Code
Project Health Dashboard
Downloadable Code Review Report

**Future Improvements**

Support multiple programming languages
AI powered automatic refactoring
Integration with GitHub pull requests
Security vulnerability detection
CI/CD integration for automated code reviews

**License**
MIT License