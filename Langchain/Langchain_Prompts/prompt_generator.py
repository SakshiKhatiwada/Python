from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematcal Details:
    - Include relevant mathematical equations if present in the paper
    - Explain the mathematical concepts using simple, intuitive code snippets where applicabe.

2. Analogies:
    - Use relatable analogies to simplify complex ideas.

If certain information is not available in the paper, respond with "Insufficient information available" instead of guessing.
""",
input_variables = ["paper_input", "style_input", "length_input"],
validate_template = True # validates if all the placeholder variable names are in the variable input_variables
)

template.save('Langchain/Langchain_Prompts/template.json')
# template.save('template.json')