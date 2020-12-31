import discord
import asyncio

client = discord.Client()

token="NzkzMDk1NDQ0MjQ2NjkxODcx.X-nRsA.QYiXa-LeBOhziZdKa-nRYoj4aQg" 


@client.event
async def on_ready():
    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('봇이 활동중에 표시될 이름')
    await Client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("할말")
    if message.content.startswith("준영"):
        await message.channel.send("돼지")
    if message.content.startswith(""):
        await message.channel.send("돼지")
    

    
client.run("NzkzMDk1NDQ0MjQ2NjkxODcx.X-nRsA.QYiXa-LeBOhziZdKa-nRYoj4aQg")