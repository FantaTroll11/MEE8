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
        await bot.start("Token")

asyncio.run(main())
