import discord
from discord.ext import commands
import requests
import random

import itertools
import threading
import time
import sys
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!')
t = threading.Thread(target=animate)
t.start()
#long process here
time.sleep(10)
done = True

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='c!', intents=intents)
users = {}

@client.event
async def on_ready():
    print(f'\nLogged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Example command: !hello
    if message.content.startswith('c!hello'):
        await message.channel.send("Hello!, I am a Discord bot developed and owned by **CodeIQ on GitHub**")

    if message.content.startswith('c!code-idea'):
        project_ideas = ['Build a chatbot',
                         'Create a weather application',
                         'Develop a task management tool',
                         'Build a cryptocurrency tracker',
                         'Create a recipe recommendation system',
                         'Develop a music streaming service',
                         'Build a personal finance manager',
                         'Create a language learning application',
                         'Develop a quiz game',
                         'Build a social media dashboard',
                         'Make a website',
                         'Maker a DiscoRD bOT']
        project_idea = random.choice(project_ideas)
        await message.channel.send(f'__Code Project Idea:__ **{project_idea}**')




client.run('ENTER_TOKEN')
