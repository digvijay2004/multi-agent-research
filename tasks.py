from crewai import Task

def create_research_task(researcher, topic):
    return Task(
        description=f"""Research the following topic thoroughly: {topic}
        
        Your research should include:
        - Key concepts and definitions
        - Current trends and developments
        - Important facts and statistics
        - Notable examples and use cases
        
        Be comprehensive and accurate in your research.""",
        expected_output="""A comprehensive research report with key facts, 
        trends, statistics, and examples related to the topic.""",
        agent=researcher
    )

def create_analysis_task(analyst, topic):
    return Task(
        description=f"""Analyze the research findings about: {topic}
        
        Your analysis should:
        - Identify the most important insights
        - Highlight key trends and patterns
        - Evaluate the significance of findings
        - Provide critical observations
        
        Be objective and data-driven in your analysis.""",
        expected_output="""A structured analysis with key insights, 
        trends, patterns, and critical observations.""",
        agent=analyst
    )

def create_writing_task(writer, topic):
    return Task(
        description=f"""Write a clear and engaging research report about: {topic}
        
        The report should include:
        - Executive Summary
        - Key Findings
        - Detailed Analysis
        - Trends and Implications
        - Conclusion
        
        Write in a professional yet accessible style.""",
        expected_output="""A well-structured research report with clear sections,
        professional writing, and actionable insights.""",
        agent=writer
    )