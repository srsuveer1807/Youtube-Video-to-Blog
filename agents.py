
from crewai import Agent
from langchain_cohere import ChatCohere
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ['COHERE_API_KEY'] = os.getenv('COHERE_API_KEY')
os.environ['COHERE_MODEL_NAME'] = 'command-r7b-12-2024'
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', 'dummy-key')

# Create LLM
llm = ChatCohere(model='command-r7b-12-2024')

# Research Agent
def create_blog_researcher():
    return Agent(
        role='Content Researcher from YouTube',
        goal='Research relevant video content for the topic {topic} from the specified YouTube channel',
        verbose=True,
        memory=True,
        backstory='You are skilled at extracting valuable content from YouTube videos across various topics.',
        llm=llm,
        tools=[],  # Tool will be added at Task level
        allow_delegation=True
    )

# Writing Agent
def create_blog_writer():
    return Agent(
        role='Content Writer',
        goal='Write an engaging and informative blog post about the topic {topic} using the research data.',
        verbose=True,
        memory=True,
        backstory='You turn insights into well-structured and reader-friendly blogs for any domain.',
        llm=llm,
        tools=[],
        allow_delegation=False
    )

