from capture.network_capture import capture_network_calls
from process.workflow_parser import parse_logs
from output.diagram_generator import generate_diagram
from output.pdf_generator import create_pdf

def main():
    city = input("Enter city name to search: ").strip()
    print("Capturing network calls...")
    logs = capture_network_calls(city)

    print("Parsing logs...")
    workflows = parse_logs(logs)

    print("Generating sequence diagram...")
    generate_diagram(workflows)

    print("Creating workflow documentation PDF...")
    create_pdf(workflows)

    print("Workflow documentation generated successfully!")

if __name__ == "__main__":
    main()

