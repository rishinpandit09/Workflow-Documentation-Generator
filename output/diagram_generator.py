from graphviz import Digraph


def generate_diagram(workflows):
    dot = Digraph()

    for i, workflow in enumerate(workflows):
        duration = workflow['response_time'] - workflow['timestamp'] if workflow['response_time'] else 'N/A'
        node_label = f"{workflow['method']} {workflow['url']}\nStatus: {workflow['response_status']}\nDuration: {duration}"

        # Highlight failed requests
        if workflow['response_status'] and int(workflow['response_status']) >= 400:
            dot.node(f"Step {i + 1}", node_label, color='red')
        else:
            dot.node(f"Step {i + 1}", node_label)

        if i > 0:
            dot.edge(f"Step {i}", f"Step {i + 1}")

    diagram_path = "resources/workflow_diagram"
    dot.render(diagram_path, format='png', cleanup=True)
    print(f"Diagram saved at {diagram_path}.png")
