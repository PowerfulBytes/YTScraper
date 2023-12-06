from googleapiclient.discovery import build
import sys
from dotenv import dotenv_values

def scrape_youtube_videos(genre: str):
    """
    Scrapes YouTube videos based on a given genre and saves the video titles and URLs to a text file.

    Args:
        genre (str): The genre of the videos to be scraped.

    Returns:
        None
    """
    # Load the environment variables from the .env file
    config = dotenv_values("YOUTUBE_TOKEN.env")
    token = config['YOUTUBE_TOKEN']

    # Set up the YouTube Data API
    api_key = token
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Define the search parameters
    search_keyword = genre
    max_results = 50

    # Send a search request to the YouTube Data API
    request = youtube.search().list(
        part="snippet",
        maxResults=max_results,
        q=search_keyword,
        type="video"
    )
    response = request.execute()

    # Open the output file with utf-8 encoding
    with open(f"{genre}.txt", "w", encoding="utf-8") as f:
        # For each search result
        for item in response['items']:
            # Get the video title and URL
            title = item['snippet']['title']
            video_id = item['id']['videoId']
            url = f"https://www.youtube.com/watch?v={video_id}"

            # Write the title and URL to the output file
            f.write(f"{title}: {url}\n")
