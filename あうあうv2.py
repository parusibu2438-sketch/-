import discord
import random
import time
import re
from bot_token import TOKEN


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

user_cooldowns = {}

@client.event
async def on_ready():
    print(f"あうあう")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if random.random() < 0.01:
        await message.channel.send("あうあう")
        return

    stripped_content = message.content.strip()
    if stripped_content.endswith("？") or stripped_content.endswith("?"):
        if random.random() < 0.03:
            await message.channel.send("あう！")
            return

    if message.content in ["あうあう", "あう", "あうー"]:
        await message.channel.send(message.content)
        return
    
    if re.fullmatch(r'[あ、う！!？?AUau‼️⁉️]+', message.content):
        current_time = time.time()
        user_id = message.author.id

        if user_id in user_cooldowns:
            if current_time - user_cooldowns[user_id] < 5:
                return
        user_cooldowns[user_id] = current_time

        middle_length = random.randint(1, 7)
        middle = "".join(random.choice(["あ", "う"]) for _ in range(middle_length))
        reply = "あ" + middle + "う"
        await message.channel.send(reply)
        return

    if "あう" in message.content:
        await message.channel.send("あうー！")
        return

client.run(TOKEN)
