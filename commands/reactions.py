import os
from discord.ext import commands
import discord
from utils.usual_functions import readJson, writeJson

class Reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='poll', help="cria uma enquete. uso: 'u!poll [pergunta sim ou não]'")
    async def poll(self, ctx, *question):
        await ctx.channel.purge(limit=1)
        message = await ctx.send(f"```Enquete: \n{' '.join(question)}```\n**✅ = Sim**\n**❎ = Não**")
        await message.add_reaction('✅')
        await message.add_reaction('❎')
        data = readJson('polls')
        new_poll = { 'message_id': message.id }
        data['values'].append(new_poll)
        writeJson('polls', data)

    @commands.command(name="cargos")
    async def cargos_por_reacao(self, ctx, emoji=None, cargo:discord.Role=None, *, message=None):
        role = discord.utils.find(lambda r: r.id == 544691816147058688, ctx.message.guild.roles)
        if not role in ctx.author.roles:
            await ctx.send(f'Olá <@{ctx.author.id}>, O comando só pode ser usado por moderadores.')
            return

        if emoji == None:
            embed=discord.Embed(title='TeamEXP',description=f'*Escolha um emoji, cargo e mensagem:* {os.linesep}ex: /presente [emoji] [cargo] [mensagem]')
            await ctx.send(embed=embed)  
        else:
            if cargo ==None:
                embed=discord.Embed(title='TeamEXP',description=f'*Escolha um emoji, cargo e mensagem:**{os.linesep}ex: /presente [emoji] [cargo] [mensagem]')
                await ctx.send(embed=embed) 
            else:
                if message ==None:
                    embed=discord.Embed(title='TeamEXP',description=f'**Escolha um emoji, cargo e mensagem:* {os.linesep}ex: /presente [emoji] [cargo] [mensagem]')
                    await ctx.send(embed=embed)
                else:
                    embed=discord.Embed(description=f'**{message}**')
                    await ctx.message.delete()
                    enviar= await ctx.send(embed=embed)
                    await enviar.add_reaction(emoji)

                    data = readJson('cargos')
                    new_react_role = {
                        'role_name':cargo.name,
                        'role_id':cargo.id,
                        'emoji':emoji,
                        'message_id':enviar.id }
                    data['values'].append(new_react_role)
                    writeJson('cargos', data)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        data = readJson('cargos')
        for x in data['values']:
            if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                role = discord.utils.get(self.bot.get_guild(payload.guild_id).roles,id=x['role_id'])
                await self.bot.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.bot:
            pass
        else:
            data = readJson('cargos')
            for x in data['values']:
                if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                    role = discord.utils.get(self.bot.get_guild(payload.guild_id).roles,id=x['role_id'])
                    await payload.member.add_roles(role)
            
            data = readJson('polls')
            for x in data['values']:
                if "\u2705" == payload.emoji.name and x['message_id'] == payload.message_id:
                    channel = self.bot.get_channel(payload.channel_id)
                    message = await channel.fetch_message(payload.message_id)
                    user = self.bot.get_user(payload.user_id)
                    await message.remove_reaction('❎', user)
                elif "\u274e" == payload.emoji.name and x['message_id'] == payload.message_id:
                    channel = self.bot.get_channel(payload.channel_id)
                    message = await channel.fetch_message(payload.message_id)
                    user = self.bot.get_user(payload.user_id)
                    await message.remove_reaction('✅', user)


def setup(bot):
    bot.add_cog(Reactions(bot))