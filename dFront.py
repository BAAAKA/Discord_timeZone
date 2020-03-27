from timeZoneBot import *
import os
import discord
import re

# GetToken
token = os.environ['discordTokenTimeBot']
print("Token: {}".format(token))

client = discord.Client()
filename = "data.txt"

array = {}

@client.event
async def on_ready():
    array = {}
    #inputTime("KAWAII BAAAKA", "12:24", "data.txt")
    #inputTime("Someone else", "20:52", "data.txt")
    tArray = readFile(filename)
    request("KAWAII BAAAKA", "20:58", tArray)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if re.findall(r'!\d{1,2}', message.content.lower()):
        matches = re.findall(r'!(\d{1,2}:?[0-9]?[0-9]?)', message.content.lower())
        print(matches[0])

        tArray = readFile(filename)
        request("KAWAII BAAAKA", matches[0], tArray)
        await message.channel.send('<3 :3')


client.run(token)