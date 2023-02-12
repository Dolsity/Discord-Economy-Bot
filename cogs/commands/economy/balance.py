from nextcord.ext import commands
from nextcord import Interaction, SlashOption, Embed, Member, slash_command
import datetime
from utils import (
    # Colors
    Defualt_Color,
    Careful_Color,
    # Databases
    profile
)

class Balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name="balance", 
        description="Check your balance or the balances of others", 
        dm_permission=False, force_global=True
    )
    async def balance(
        self, interaction : Interaction, 
        user: Member = SlashOption(
            description="Please select a user", required=False
        )):
        
        if user is None:
            await interaction.response.defer()
            embed = Embed(
                description="Connecting to database...",
                color=Defualt_Color
            )
            embed.set_author(
                name=interaction.user.name,
                icon_url=interaction.user.display_avatar
            )
            message = await interaction.send(embed=embed)

            author_data = profile.find_one({"_id": interaction.user.id})
            
            if author_data is None:
                await message.delete()
                embed = Embed(
                    description="Something went wrong!\nPlease try again.", 
                    color=Careful_Color
                )
                embed.set_author(
                    name="Data not found!",
                    icon_url=interaction.user.display_avatar
                )
                return await interaction.send(embed=embed, ephemeral=True)

            bank = author_data['bank']
            wallet = author_data['wallet']
            total = bank + wallet

            embed.description=f"**Wallet:** ${wallet:,}\n**Bank:** ${bank:,}"
            embed.set_author(
                name=f"{interaction.user.name}'s balance", 
                icon_url=interaction.user.display_avatar
            )
            embed.timestamp = datetime.datetime.today()
            embed.set_footer(text=f'Total: ${total:,}')
            return await message.edit(embed=embed)
        else:
            await interaction.response.defer()
            embed = Embed(
                description="Connecting to database...",
                color=Defualt_Color
            )
            embed.set_author(
                name=user.name,
                icon_url=user.display_avatar
            )
            message = await interaction.send(embed=embed
            )
            user_data = profile.find_one({"_id": user.id})
            
            if user_data is None:
                await message.delete()
                embed = Embed(
                    description=f"{user.mention} doesn't have a profile", 
                    color=Careful_Color
                )
                embed.set_author(
                    name="Profile not found!",
                    icon_url=interaction.user.display_avatar
                )
                return await interaction.send(embed=embed, ephemeral=True)

            bank = user_data['bank']
            wallet = user_data['wallet']
            total = bank + wallet
            
            embed.description=f"**Wallet:** ${wallet:,}\n**Bank:** ${bank:,}"
            embed.set_author(
                name=f"{user.name}'s balance", 
                icon_url=user.display_avatar
            )
            embed.timestamp = datetime.datetime.today()
            embed.set_footer(text=f'Total: ${total:,}')
            return await message.edit(embed=embed)
    
def setup(bot):
    bot.add_cog(Balance(bot))