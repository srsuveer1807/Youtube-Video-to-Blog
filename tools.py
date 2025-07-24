from dotenv import load_dotenv
import os
from crewai_tools import YoutubeChannelSearchTool, YoutubeVideoSearchTool

load_dotenv()

def get_yt_tool(input_type, value):
    if input_type == "Channel":
        return YoutubeChannelSearchTool(youtube_channel_handle=value)
    elif input_type == "Video Link":
        return YoutubeVideoSearchTool(video_url=value)
    else:
        raise ValueError("Unsupported YouTube input type")
