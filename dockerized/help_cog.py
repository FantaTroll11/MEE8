## script name: help_cog.py

import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.help_message = """
```
General commands:
/Help - displays all the available commands
/Play <keywords> - finds the song on youtube and plays it in your current channel. Will resume playing the current song if it was paused
/queue - displays the current music queue
/skip - skips the current song being played
/Clear - Stops the music and clears the queue
/Leave - Disconnected the bot from the voice channel
/Pause - pauses the current song being played or resumes if already paused
/Resume - resumes playing the current song
```
"""
        self.text_channel_text = []
    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_text.append(channel)
        await self.send_to_all(self.help_message)
        
    async def semd_to_all(self,msg):
        for text_channel in self.text_channel_text:
            await text_channel.send(msg)

    @commands.command(name="helpme", aliases = ["h"], help= "Displays all avaiable commands")
    async def Help(self,ctx):
        await ctx.send(self.help_message)