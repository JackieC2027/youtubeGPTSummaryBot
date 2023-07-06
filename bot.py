import discord
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
import openai

openai.api_key = "REDACT"
TOKEN = 'REDACT'

# Function to get the response using OpenAI Chat API
def getResponse(url):
    # get videoID from link
    parsedUrl = urlparse(url)
    qsDict = parse_qs(parsedUrl.query)
    videoId = qsDict.get('v')
    videoId = videoId[0]

    # uses the videoID to get transcript 
    finalTranscript = [] 
    videoText = YouTubeTranscriptApi.get_transcript(videoId, languages=['en'])
    for words in videoText:
        output = words['text']
        finalTranscript.append(output)
    summary = str(finalTranscript)

    messages = [
        {"role": "system", "content": 'You are an extremely advanced summarization assistant. Given a list of strings, I want you to be able to summerize the strings into an informative paragraph with specific examples from the text. Only one paragraph for the response.'},
        {"role": "user", "content": summary}
    ]
    
    # Call OpenAI API to generate response
    gptResponse = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=messages)
    summaryResponse = gptResponse["choices"][0]["message"]["content"]

    return summaryResponse

# Function to send the response message
async def sendMessage(message, user_message, is_private):
    try:
        response = getResponse(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username} said: "{user_message}" ({channel})')

    valid_command = False
    user_message = user_message.split()

    # Check for valid commands
    if user_message[0] == "$transcribe":
        valid_command = True
        user_message = " ".join(user_message[1:])
        await sendMessage(message, user_message, is_private=False)

    elif user_message[0] == "$transcribePM":
        valid_command = True
        user_message = " ".join(user_message[1:])
        await sendMessage(message, user_message, is_private=True)

client.run(TOKEN)
