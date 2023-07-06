# youtubeGPTSummaryBot
This project is a Discord bot that can transcribe and summarize YouTube videos. It utilizes the YouTubeTranscriptApi and OpenAI's GPT-3.5 Turbo model for natural language processing. By connecting to Replit's Paid Plan, the script is continuously running on a live server, allowing the bot to function without the presence of a physical tab.

# Prerequisites
Before running the bot, make sure you have the following prerequisites:

- Python 3.x
- discord.py library
- youtube-transcript-api library
- openai library

# Installation
1. Clone this repository to your local machine.
2. Install the required dependencies by running the following command:

```pip install -r requirements.txt```

# Preview
<h2>Public Channel Transcription</h2>
<img width="1102" alt="Screenshot 2023-07-06 at 1 24 47 AM" src="https://github.com/JackieC2027/youtubeGPTSummaryBot/assets/110410844/f53b9290-eef7-492c-ab23-2614dc2cd47e">

<h2>Invalid Formatting</h2>
<img width="814" alt="Screenshot 2023-07-06 at 1 25 48 AM" src="https://github.com/JackieC2027/youtubeGPTSummaryBot/assets/110410844/58b01b12-7bcf-4457-833e-4b1ba55e6fc3">

<h2>Private Format Transcription</h2>
<img width="811" alt="Screenshot 2023-07-06 at 1 25 05 AM" src="https://github.com/JackieC2027/youtubeGPTSummaryBot/assets/110410844/a7e9a067-cdff-4038-8ed3-62f0999872b2">

<h2>Transcription for Private Bot Usage</h2>
<img width="750" alt="Screenshot 2023-07-06 at 1 25 32 AM" src="https://github.com/JackieC2027/youtubeGPTSummaryBot/assets/110410844/ec32f842-cc86-4750-9e9d-3ccad46a14e7">

<h2>Console for Bot Logs</h2>
<img width="703" alt="Screenshot_2023-07-06_at_1 26 57_AM" src="https://github.com/JackieC2027/youtubeGPTSummaryBot/assets/110410844/a8544b9f-afa5-465e-b5d6-d29706ffbdbe">

# Configuration
Obtain the required API keys:

- YouTube Data API key: YouTube Data API Documentation
- OpenAI API key: OpenAI API Documentation

Replace 'REDACT' with your OpenAI API key:
  - openai.api_key = "YOUR_OPENAI_API_KEY"
Replace 'REDACT' with your Discord bot token:
  - TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

# Usage
Add the bot to your Discord server using the Discord Developer Portal.
Run the bot script using the following command:
```python bot.py```

The bot will be online and ready to transcribe and summarize YouTube videos.

# Commands
The bot recognizes the following commands:

- $transcribe [YouTube Video URL]: Transcribes and summarizes the provided YouTube video. The summary will be sent as a message in the current channel.

- $transcribePM [YouTube Video URL]: Transcribes and summarizes the provided YouTube video. The summary will be sent as a private message to the user who invoked the command.

# Note
The bot uses OpenAI's GPT-3.5 Turbo model for text summarization, which requires an API key and may have usage limitations depending on your OpenAI subscription.

# Credits
This project uses the following libraries and APIs:

- discord.py - A Python library for creating Discord bots.
- youtube-transcript-api - A Python library for retrieving YouTube video transcripts.
- OpenAI API - OpenAI's powerful language model for natural language processing.
