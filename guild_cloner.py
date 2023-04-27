import os
import random
import discord
from discord.ext import commands
from aiohttp import ClientSession
from aiohttp_socks import ProxyConnector

TOKEN = ''

bot = commands.Bot(command_prefix='!')

async def get_random_proxy():
    with open("proxy.txt", "r") as f:
        proxies = f.readlines()
        return random.choice(proxies).strip()

async def delete_existing_content(guild):
    for category in list(guild.categories):
        await category.delete()

    for channel in list(guild.channels):
        await channel.delete()

    for role in list(guild.roles)[1:]:
        await role.delete()

async def clone_guild(from_guild_id, to_guild_id):
    from_guild = bot.get_guild(from_guild_id)
    to_guild = bot.get_guild(to_guild_id)

    await delete_existing_content(to_guild)

    categories = {}
    for cat in from_guild.categories:
        new_cat = await to_guild.create_category(cat.name)
        categories[cat.id] = new_cat

    for channel in from_guild.channels:
        cat = categories.get(channel.category_id)
        await to_guild.create_text_channel(channel.name, category=cat)
        await asyncio.sleep(0.4)

    for role in from_guild.roles:
        await to_guild.create_role(
            name=role.name,
            permissions=role.permissions,
            colour=role.color,
            hoist=role.hoist,
            mentionable=role.mentionable
        )
        await asyncio.sleep(0.4)

@bot.event
async def on_ready():
    print(f'{bot.user} is connected.')

    from_guild_id = int(input("Enter from_guild_id: "))
    to_guild_id = int(input("Enter to_guild_id: "))

    proxy = await get_random_proxy()
    connector = ProxyConnector.from_url(proxy)
    async with ClientSession(connector=connector) as session:
        await clone_guild(from_guild_id, to_guild_id)

bot.run(TOKEN)
