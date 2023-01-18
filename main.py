import discord
from discord.ext import commands
from nltk.chat.util import Chat, reflections

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["My name is Bot", "I am Bot, nice to meet you!"]
    ],
    [
        r"how are you?",
        ["I'm doing good, thanks for asking!", "I'm great, how about you?"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind"]
    ],
    [
        r"I am fine",
        ["Great to hear that!"]
    ],
    [
        r"quit",
        ["BBye take care. It was nice talking to you :) "]
    ],
]

chatbot = Chat(pairs, reflections)

@bot.command(name='chat')
async def chat(ctx):
    await ctx.send("Hi, I am a chatbot. How can I help you today?")
    while True:
        message = await bot.wait_for('message')
        if message.author == bot.user:
            continue
        if message.content.lower() == "quit":
            await ctx.send("BBye take care. It was nice talking to you :)")
            break
        else:
            await ctx.send(chatbot.respond(message.content))

bot.run('YOUR_BOT_TOKEN')
