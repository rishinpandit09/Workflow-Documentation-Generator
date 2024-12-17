from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(workflows):
    c = canvas.Canvas("resources/workflow_documentation.pdf", pagesize=letter)
    c.drawString(100, 750, "Workflow Documentation")

    y_position = 700
    for i, workflow in enumerate(workflows):
        c.drawString(100, y_position, f"Step {i+1}: {workflow['method']} {workflow['url']}")
        c.drawString(120, y_position-20, f"Status: {workflow['response_status']}")
        c.drawString(120, y_position-40, f"Response Time: {workflow['response_time']}")
        y_position -= 60
        if y_position < 100:
            c.showPage()
            y_position = 750

    c.save()
    print("PDF report saved at resources/workflow_documentation.pdf")
