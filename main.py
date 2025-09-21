import discord
from discord.ext import commands

TOKEN = "BOT_TOKEN"

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập thành công với tên: {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "hello":
        await message.channel.send("tui đây có chiện j hogg")

    await bot.process_commands(message)

bot.run(TOKEN)
