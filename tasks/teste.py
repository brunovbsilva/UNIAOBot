import asyncio
import discord
from discord.ext import commands
from datetime import datetime 

class Teste(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     self.bot.loop.create_task(self.current_time())

    # async def current_time(self):
    #     while(True):
    #         channel = self.bot.get_channel(1002400564241514587)
    #         horario = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
    #         await channel.send(horario)
    #         await asyncio.sleep(2)

def setup(bot):
    bot.add_cog(Teste(bot))