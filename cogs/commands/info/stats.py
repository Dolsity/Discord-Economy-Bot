from math import floor
from datetime import datetime
from nextcord import slash_command, Interaction, Embed
from nextcord.ext import commands

from utils import Defualt_Color, format_number


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name="ping", 
        description="Test server latency by measuring how long it takes to edit a message",
        dm_permission=False, force_global=True
    )
    async def ping(self, interaction : Interaction) -> None:
        await interaction.response.defer()
        embed = Embed(
            title=":ping_pong: Pong!", color=Defualt_Color
        )
        embed.set_thumbnail(url=self.bot.user.display_avatar)
        embed.description = "Latency: testing..."

        b = datetime.utcnow()

        await interaction.send(embed=embed)

        ping = floor((datetime.utcnow() - b).total_seconds() * 1000)
        embed.description = ""
        embed.add_field(
            name="Message Latency", value=f"`{format_number(ping)}ms`"
        )
        embed.add_field(
            name="API Latency", value=f"`{format_number(floor(self.bot.latency*1000))}ms`"
        )
        return await interaction.edit_original_message(embed=embed)

def setup(bot):
    bot.add_cog(Stats(bot))