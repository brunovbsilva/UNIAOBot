import imp
from discord.ext import commands

class Reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='poll')
    async def poll(self, ctx, *question):
        await ctx.channel.purge(limit=1)
        message = await ctx.send(f"```Enquete: \n{' '.join(question)}```\n**✅ = Sim**\n**❎ = Não**")
        await message.add_reaction('✅')
        await message.add_reaction('❎')

    @commands.command(name='cargos', help='só pode ser usado no canal de cargos')
    async def alo(self, ctx, *expression):
        if ctx.channel.id == 1001617719730393128:
            await ctx.channel.purge(limit=1)
            message = await ctx.send(f"```{' '.join(expression)}```\n **🇺 = @união BASE**\n **🇨 = @CINEMINHA**\n **🇴 = @OTAKU**")
            await message.add_reaction("🇺")
            await message.add_reaction("🇨")
            await message.add_reaction("🇴")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.message.channel.id == 1001617719730393128 and reaction.message.author == self.bot.user and user != self.bot.user:
            if reaction.emoji == "🇺":
                role = user.guild.get_role(690982391073734716) # união base
                await user.add_roles(role)
            if reaction.emoji == "🇨":
                role2 = user.guild.get_role(874103747071053855) # cineminha
                await user.add_roles(role2)
            if reaction.emoji == "🇴":
                role3 = user.guild.get_role(932443081427538000) # otaku
                await user.add_roles(role3)

def setup(bot):
    bot.add_cog(Reactions(bot))