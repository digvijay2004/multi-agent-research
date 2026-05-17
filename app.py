import gradio as gr
from crew import run_research_crew

def research(topic):
    if not topic or topic.strip() == "":
        return "Please enter a research topic."
    try:
        result = run_research_crew(topic)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

demo = gr.Interface(
    fn=research,
    inputs=gr.Textbox(
        label="Research Topic",
        placeholder="e.g. Latest trends in LLM fine-tuning",
        lines=2
    ),
    outputs=gr.Textbox(
        label="Research Report",
        lines=20
    ),
    title="Multi-Agent AI Research Assistant",
    description="""A multi-agent AI system powered by CrewAI and Groq LLM.
    Three specialized agents collaborate to research any topic:
    Agent 1 (Researcher) gathers information,
    Agent 2 (Analyst) extracts key insights,
    Agent 3 (Writer) produces a structured report.""",
    examples=[
        ["Latest trends in Large Language Models"],
        ["Applications of RAG in enterprise AI"],
        ["Future of multi-agent AI systems"]
    ]
)

if __name__ == "__main__":
    demo.launch()