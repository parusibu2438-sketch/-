import random
import re
import discord
from discord import app_commands

token = ""

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents, max_messages=10)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyClient()

@client.event
async def on_ready():
    print(f'あうあう')
    activity = discord.Activity(name="ちんちんまんまん受精卵レースを視聴中！", type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "うゆ":
        await message.channel.send("あうー！")
        return


    if message.content in ["あうあう", "あう", "あうー"]:
        await message.channel.send(message.content)
        return

    if re.fullmatch(r'[あいうえお、！!？?AUau‼️⁉️]+', message.content):
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

client.run(token)
