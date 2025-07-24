
from crewai import Task

def create_tasks(research_agent, writer_agent, yt_tool, topic):
    # Research Task
    research_task = Task(
        description=f"Find and analyze YouTube videos about '{topic}' from the given channel.",
        expected_output="A 3-paragraph research summary on the topic.",
        tools=[yt_tool],
        agent=research_agent,
    )

    # Writing Task
    write_task = Task(
        description=f"Create a blog post from the researched content about '{topic}'.",
        expected_output="A blog post summarizing and explaining the topic in an engaging way.",
        agent=writer_agent,
        tools=[yt_tool],
        async_execution=False,
        output_file='new-blog-post.md',
    )

    return research_task, write_task
