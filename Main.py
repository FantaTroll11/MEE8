## script name: Main.py

import discord
from discord.ext import commands
import os
from music_cog import music_cog
from help_cog import help_cog
import asyncio


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

bot.remove_command("help")
async def main():
    async with bot:
        await bot.add_cog(music_cog(bot))
        await bot.add_cog(help_cog(bot))
        await bot.start("MTEzMDUwMjQ4NjM3ODE3MjQzNg.GNXZc9.DkZA6UkF_o3dzErO1ooE-BEONuS-6P1r8i6xSA")

asyncio.run(main())