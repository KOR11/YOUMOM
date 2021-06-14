from ast import Await
import discord, asyncio, datetime, pytz

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("V1 UPDATE"))

@client.event
async def on_message(message):
    if message.content == "안녕하세요": # 메세지 감지
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        


    if message.content == "라아 못생김":     
        await message.channel.send ("{} | {}, ㅇㅈ".format(message.author, message.author.mention))
        


    if message.content == "라아가 좋아하는거": # 메세지 감지
        embed = discord.Embed(title="라아 코어", description="",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name="1장",  value="라아 코어는 로블록스, 채팅 봇을 위해 만들어졌습니다", inline=False)
        embed.add_field(name="2장", value="라아는 봇을 만드는걸 좋아합니다", inline=False)
        embed.add_field(name="3장", value="라아는 친구들과 봇을 만드는걸 좋아합니다.", inline=False)
        embed.add_field(name="4장", value="라아는 친구들을 아낍니다", inline=False)
       
        embed.set_footer(text="Bot Made by. 그냥 라아임", icon_url="https://cdn.discordapp.com/attachments/851155749353816077/853535951733260298/i014450146843.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/851155749353816077/853535951733260298/i014450146843.gif")
        await message.channel.send (embed=embed)




    if message.content == "라아 뜻":     
        await message.channel.send ("{} | {}, 라아는 라군 + 아파 .".format(message.author, message.author.mention))
    
    if message.content == "저 기여미죠":
        await message.channel.send ("{} | {}, 응 아니야!".format(message.author, message.author.mention))


    if message.content == "로블굿 잘생김":     
        await message.channel.send ("{} | {}, 라아는 못생겼고 로블굿은 잘생김 .".format(message.author, message.author.mention))


# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('ODUzNTMyNjE5MDUxNDk5NTMx.YMWwMg.Ikecd85ObzipLbHLFq9MopD-05o')