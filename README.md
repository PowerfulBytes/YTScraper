# Youtube Video Scraper

This Python script allows you to scrape YouTube videos based on a specified genre and save their titles and URLs to a text file.

Prerequisites
Before running the script, make sure you have the following:

YouTube API Key:

Obtain an API key from the Google Developers Console.
Enable the YouTube Data API v3 for your project.
Environment Variables:

Create a .env file with the following content:
YOUTUBE_TOKEN=your_api_key_here

Replace your_api_key_here with your actual YouTube API key.
#Installation
Clone this repository:

git clone https://github.com/your-username/youtube-video-scraper.git

Install the required Python packages:

pip install -r requirements.txt

Usage
Run the script:

python scrape_youtube_videos.py --genre <your_genre>

Replace <your_genre> with the desired genre (e.g., “music,” “gaming,” etc.).

The script will fetch YouTube videos related to the specified genre and save their titles and URLs to a text file named <your_genre>.txt.

Example Output
For the genre “music,” the output file will contain entries like:

Video Title 1: https://www.youtube.com/watch?v=video_id_1
Video Title 2: https://www.youtube.com/watch?v=video_id_2
...

Contributing
Email to ask about contribution permission

License
This project is licensed under a custom License - see the LICENSE file for details.
