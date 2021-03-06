import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from util.CustomHelpCommand import CustomHelpCommand

load_dotenv(".env")
intents = discord.Intents.all()

client = commands.Bot(command_prefix="!", intents=intents, status=discord.Status.do_not_disturb,
                      help_command=CustomHelpCommand(), voice_client=discord.VoiceClient)

for filename in os.listdir("cogs"):
    if filename.endswith(".py") and filename != "Nsfw.py":
        client.load_extension(f"cogs.{filename[:-3]}")


# def is_server_owner(ctx):
#     if ctx.message.author.id == 401415617032486922:
#         return True


@client.event
async def on_message(message):
    if message.author.bot:
        return

    await client.process_commands(message)


@client.command()
# @client.check(is_server_owner)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
# @client.check(is_server_owner)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


@client.command()
# @client.check(is_server_owner)
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")

# Bot token
client.run(os.getenv('BOT_TOKEN'))
