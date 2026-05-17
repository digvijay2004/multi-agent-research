from crewai import Crew, Process
from agents import create_researcher, create_analyst, create_writer
from tasks import create_research_task, create_analysis_task, create_writing_task
from dotenv import load_dotenv
import time
import os

load_dotenv()

def run_research_crew(topic: str) -> str:
    researcher = create_researcher()
    analyst = create_analyst()
    writer = create_writer()

    research_task = create_research_task(researcher, topic)
    analysis_task = create_analysis_task(analyst, topic)
    writing_task = create_writing_task(writer, topic)

    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=[research_task, analysis_task, writing_task],
        process=Process.sequential,
        verbose=True
    )

    max_retries = 3
    for attempt in range(max_retries):
        try:
            time.sleep(60)
            result = crew.kickoff()
            return str(result)
        except Exception as e:
            if "rate_limit" in str(e).lower() and attempt < max_retries - 1:
                print(f"Rate limit hit, waiting 60 seconds... (attempt {attempt + 1})")
                time.sleep(60)
            else:
                raise e
    
    return "Error: Max retries exceeded"