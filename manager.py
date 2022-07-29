import time
import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound, CommandInvokeError

class Manager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("\n"*30)
        print(f"O bot está ativo!\nConectado como {self.bot.user}")
        await self.bot.change_presence(
            status=discord.Status.idle,
            activity=discord.Game(f"u!help - para ver todos os comandos"))

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     if message.author == self.bot.user:
    #         return

    #     if message.author.id == 289888553821929483:
    #         phrases = [
    #             'ziiipt',
    #             'XIIIU',
    #             'xiiiiiiiii...',
    #             'JÁ FALEI PRA FICAR QUIETO',
    #             'XIU AI CARALHO',
    #             'quieto'
    #         ]
    #         print(f"{message.author} diz: {message.content}")
    #         await message.channel.send(f"{message.author}, {random.choice(phrases)}!")
    #         await message.delete()
       
    #     if "UNIÃO" in message.content.upper():
    #         print(f"{message.author} diz: {message.content}")
    #         await message.channel.send(f"{message.author}, não falamos da União!")
    #         await message.delete()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Há argumentos faltantes. Digite u!help para mais informações.")
        elif isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe. Digite u!help para mais informações.")
        elif isinstance(error, CommandInvokeError):
            await ctx.send("Argumentos na forma incorreta. Digite u!help para mais informações.")
        else:
            raise error

    # @commands.Cog.listener()
    # async def on_message_sent_to_channel(self, message):
    #     if message.channel.id == 1002400564241514587:
    #         await message.delete()
    
    @commands.command(name='clear', pass_context = True)
    async def clear(self, ctx, number):
        role = discord.utils.find(lambda r: r.id == 544691816147058688, ctx.message.guild.roles)
        if not role in ctx.author.roles:
            await ctx.send(f'Olá {ctx.author.name}, O comando só pode ser usado por moderadores.')
            return
        
        qtt = eval(number)
        if qtt>0:
            await ctx.channel.purge(limit=qtt+1)
        
            

def setup(bot):
    bot.add_cog(Manager(bot))