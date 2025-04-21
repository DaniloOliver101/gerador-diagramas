"""
Registry for diagram generators.
"""
from core.diagram_generators.architecture_diagram import generate_architecture_diagram
from core.diagram_generators.class_diagram import generate_class_diagram
from core.diagram_generators.component_diagram import generate_component_diagram
from core.diagram_generators.deployment_diagram import generate_deployment_diagram
from core.diagram_generators.sequence_diagram import generate_sequence_diagram
from core.diagram_generators.use_case_diagram import generate_use_case_diagram

# Dictionary mapping diagram types to their respective generator functions (English)
DIAGRAM_GENERATORS = {
    "architecture": generate_architecture_diagram,
    "classes": generate_class_diagram,
    "components": generate_component_diagram,
    "deployment": generate_deployment_diagram,
    "sequence": generate_sequence_diagram,
    "use cases": generate_use_case_diagram
}

# Dictionary mapping diagram types to their respective generator functions (Portuguese)
PT_DIAGRAM_GENERATORS = {
    "arquitetura": generate_architecture_diagram,
    "classes": generate_class_diagram,
    "componentes": generate_component_diagram,
    "implantacao": generate_deployment_diagram,
    "sequencia": generate_sequence_diagram,
    "casos de uso": generate_use_case_diagram
}
