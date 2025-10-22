import os

from dotenv import load_dotenv
from discord.ext import commands
from database import sqlquery
import discord

load_dotenv()

TOKEN = os.getenv("TOKEN")
SERVER_ID =os.getenv("SERVER_ID")
STATUS = "open"

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.tree = discord.app_commands.CommandTree(self)

    async def on_ready(self):
        print(f"✅ Logged in as {self.user} (ID: {self.user.id})")
        try:
            guild = discord.Object(id=SERVER_ID)
            self.tree.copy_global_to(guild=guild)
            synced = await self.tree.sync(guild=guild)  
            print(f"🔗 Synced {len(synced)} command(s) to guild {SERVER_ID}")
        except Exception as e:
            print(f"❌ Sync error: {e}")


bot = MyBot()

@bot.tree.command(name="greetings", description="Say hi hi to gaygay!")
async def status(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hi, {interaction.user.mention}!")


bot.run(TOKEN)