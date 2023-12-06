# Youtube Video Scraper

This Python script allows you to scrape YouTube videos based on a specified genre and save their titles and URLs to a text file.

## Prerequisites
Before running the script, make sure you have the following:

- YouTube API Key:
   > Obtain an API key from the Google Developers Console.
- Enable the YouTube Data API v3 for your project.
- Create a .env file with the following content: `YOUTUBE_TOKEN=your_api_key_here`
  > Replace your_api_key_here with your actual YouTube API key.
  
## Installation

- Clone this repository:

     `git clone https://github.com/your-username/youtube-video-scraper.git](https://github.com/PowerfulBytes/YTScraper.git`

- Install the required Python packages:

  `pip install -r requirements.txt`

## Usage

- Run the script:

   `python YTScraper.py <your_genre>`
     > Replace <your_genre> with any music to search such as '24_7 Halloween Lofi'. e.g. python YTScraper.py '24_7 Halloween Lofi'
<br>

The script will fetch YouTube videos related to the specified genre and save their titles and URLs to a text file named <your_genre>.txt.

<br>

Example Output
For the genre “music,” the output file will contain entries like:

- Video Title 1: https://www.youtube.com/watch?v=video_id_1
- Video Title 2: https://www.youtube.com/watch?v=video_id_2
<br>
This program was designed to be paired with DrunkLofiBot.py to generate a list of songs to autocomplete and play using Discord slash commands
<br>
<br>
- Link to DrunkLofiBot: https://github.com/PowerfulBytes/DrunkLofiBot
<br>
<br>

### Contributing
Email to ask about contribution permission: powerfulbytes@proton.me

### License
This project is licensed under a custom License - see the LICENSE file for details.
