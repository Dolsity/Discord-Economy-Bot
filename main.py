from nextcord.ext import commands
from nextcord import Interaction
import nextcord
from os import getenv
from extensions import initial_extensions
from utils import (
    create_user_profile,
    Bot_Owners,
)

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def process_application_commands(self, interaction: Interaction) -> None:
        await create_user_profile(
            user_id=interaction.user.id,
            user_name=interaction.user.name,
            user_tags=interaction.user.discriminator
        )
        return await super().process_application_commands(interaction)

intents = nextcord.Intents.default()
intents.members = True

bot = Bot(owner_ids = set(Bot_Owners), intents=intents)

@bot.event
async def on_ready():
    print(
        f'Logged in as {bot.user} ({bot.user.id}) ({nextcord.__version__})'
    )

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(getenv('TOKEN'), reconnect=True)