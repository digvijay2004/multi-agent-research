from crewai import Agent, LLM
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.7
    )

def create_researcher():
    return Agent(
        role="Research Specialist",
        goal="Gather comprehensive and accurate information on the given topic",
        backstory="""You are an expert researcher with years of experience 
        in finding, analyzing, and organizing information from various sources. 
        You are thorough, accurate, and always provide well-sourced information.""",
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )

def create_analyst():
    return Agent(
        role="Data Analyst",
        goal="Analyze research findings and extract the most valuable insights",
        backstory="""You are a skilled analyst who specializes in processing 
        large amounts of information and identifying the most important patterns, 
        trends, and insights. You are critical, objective, and data-driven.""",
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )

def create_writer():
    return Agent(
        role="Technical Writer",
        goal="Transform analyzed information into clear, structured, and engaging reports",
        backstory="""You are an experienced technical writer who excels at 
        converting complex information into clear, well-structured documents. 
        You write in a professional yet accessible style and always organize 
        information logically.""",
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )