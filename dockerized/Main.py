## script name: Main.py

import discord
from discord.ext import commands
import os
from music_cog import music_cog
from help_cog import help_cog
import asyncio

# Read the token from token.txt
with open("token.txt", "r") as token_file:
    TOKEN = token_file.read().strip()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

bot.remove_command("help")
async def main():
    async with bot:
        await bot.add_cog(music_cog(bot))
        await bot.add_cog(help_cog(bot))
        await bot.start(TOKEN)

asyncio.run(main())
