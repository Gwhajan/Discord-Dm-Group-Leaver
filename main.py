import discord
from discord.ext import commands
import asyncio


ryuga = commands.Bot(command_prefix="!", self_bot=True)

@ryuga.event
async def on_ready():
    print(f"Logged in as {ryuga.user} (ID: {ryuga.user.id})")
    await leave_groups()

async def leave_groups():
    left_count = 0
    for channel in ryuga.private_channels:
        if isinstance(channel, discord.GroupChannel):
            try:
                await channel.leave()
                print(f"Left group: {channel.name or 'Unnamed'}")
                left_count += 1
                await asyncio.sleep(1.5) 
            except Exception as e:
                print(f"Failed to leave group {channel.name}: {e}")
    print(f"✓ Finished. Left {left_count} group(s).")
    await ryuga.close()

ryuga.run("token", bot=False)
