import asyncio
import json
import os
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

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
       
        if "UNIÃO" in message.content.upper():
            print(f"{message.author} diz: {message.content}")
            await message.channel.send(f"{message.author}, não falamos da União!")
            await message.delete()
        
        if message.channel.id == 1002400564241514587:
            print(f"{message.author} no canal de 10 seg: {message.content}")
            await asyncio.sleep(10)
            await message.delete()

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
    
    @commands.command(name='clear', pass_context = True, help="apaga X mensagens no chat, só pode ser utilizada por moderadores. uso: 'u!clear X'")
    async def clear(self, ctx, number):
        role = discord.utils.find(lambda r: r.id == 544691816147058688, ctx.message.guild.roles)
        if not role in ctx.author.roles:
            await ctx.send(f'Olá <@{ctx.author.id}>, O comando só pode ser usado por moderadores.')
            return
        
        qtt = eval(number)
        if qtt>0:
            await ctx.channel.purge(limit=qtt+1)
    
def setup(bot):
    bot.add_cog(Manager(bot))