"""Bot module"""

from typing import TypedDict, cast
import actions
import discord
import json


class BotSettings(TypedDict):
    invite_url: str
    token: str


with open("settings.json", encoding="utf-8") as settings:
    settings = cast(BotSettings, json.load(settings))

INVITE_URL: str = settings["invite_url"]
TOKEN: str = settings["token"]


def run_discord_bot():
    """Runs Botchy"""
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")
        print(f"The invite url is {INVITE_URL}")

    @client.event
    async def on_message(message: discord.Message):
        if message.author == client.user:
            return

        print(f'{message.author} said: "{message.content}" on #{message.channel}')

        await actions.execute(message)

    client.run(TOKEN)
