from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report(data, output_file="code_review_report.pdf"):

    c = canvas.Canvas(output_file, pagesize=letter)

    y = 750

    c.setFont("Helvetica", 14)
    c.drawString(50, y, "AI Code Review Report")

    y -= 40
    c.setFont("Helvetica", 12)

    c.drawString(50, y, f"Files analyzed: {data['files_analyzed']}")
    y -= 20

    c.drawString(50, y, f"Average quality score: {data['average_quality_score']}")
    y -= 20

    c.drawString(50, y, f"Total issues: {data['total_issues']}")

    y -= 40
    c.drawString(50, y, "File Reports")
    y -= 20

    for file in data["file_reports"]:

        text = f"{file['file']}  |  Score: {file['quality_score']}  |  Issues: {file['issues_found']}"
        c.drawString(50, y, text)
        y -= 20

        if y < 100:
            c.showPage()
            y = 750

    c.save()

    return output_file