import requests
import random
import itertools
import asyncio
import sys
from interactions import Client, Intents, listen, slash_command, SlashContext
from interactions.api.events import Component, Error
from interactions.ext import prefixed_commands



bot = Client(
    intents=Intents.DEFAULT | Intents.MESSAGE_CONTENT,
    sync_interactions=True,
    asyncio_debug=True,
)

@bot.event
async def on_ready():
    print(f'\nLogged in as {bot.user}')
    global done
    done = False
    await animate()

    
from interactions.api.events import Error

@listen()
async def on_error(error: Error):
    await bot.get_channel(1110662656475537429).send(f"```\n{error.source}\n{error.error}\n```")
    
@slash_command(name="hello", description="Say hello!")
async def hello(ctx: SlashContext):
    await ctx.send("Hello!, I am a Discord bot developed and owned by **CodeIQ on GitHub**")
    
@slash_command(name="help", description="Get help!")
async def help(ctx: SlashContext):
    embeds = [Embed("The best place to learn python coding with our outstanding educational service dedicated to providing a coding education to individuals seeking to master programming. Our easy to follow courses and guides empower learners of all backgrounds with the skills and confidence needed to thrive in the digital world. Discover the power of coding with PyIQ and unlock endless opportunities for growth and success in the ever-evolving tech industry. Let's embark on this transformative learning journey together!"), Embed("The best place to learn python coding with our outstanding educational service dedicated to providing a coding education to individuals seeking to master programming. Our easy to follow courses and guides empower learners of all backgrounds with the skills and confidence needed to thrive in the digital world. Discover the power of coding with PyIQ and unlock endless opportunities for growth and success in the ever-evolving tech industry. Let's embark on this transformative learning journey together!"), Embed("The best place to learn python coding with our outstanding educational service dedicated to providing a coding education to individuals seeking to master programming. Our easy to follow courses and guides empower learners of all backgrounds with the skills and confidence needed to thrive in the digital world. Discover the power of coding with PyIQ and unlock endless opportunities for growth and success in the ever-evolving tech industry. Let's embark on this transformative learning journey together!")]
    paginator = Paginator.create_from_embeds(bot, *embeds)
@slash_command(name="project_idea", description="Get a project idea!")
async def project(ctx: SlashContext):
    project_ideas = ['Build a chatbot', 'Create a weather application', 'Develop a task management tool', 'Build a cryptocurrency tracker', 'Create a recipe recommendation system', 'Develop a music streaming service', 'Build a personal finance manager', 'Create a language learning application', 'Develop a quiz game', 'Build a social media dashboard', 'Make a website', 'Make a Discord bot']
    project_idea = random.choice(project_ideas)
    await ctx.send(f'__Code Project Idea:__ **{project_idea}**')

bot.start('token')
