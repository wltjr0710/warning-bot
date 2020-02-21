import discord
import openpyxl

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game=discord.Game("warning")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("/뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.add_roles(role)

    if message.content.startswith("/언뮤트"):
        author = message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.remove_roles(role)

    if message.content.startswith("/경고"):
        author = message.guild.get_member(int(message.content[4:22]))
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(author.id):
                sheet["B" + str(i)].value = int(sheet["A" + str(i)].value) + 1
                file.save("경고.xlsx")
                if sheet["B" + str(i)].value == 3:
                    await message.guild.ban(author)
                    await message.channel.send("경고 3회 누적입니다. 서버에서 추방합니다.")
                else:
                    await message.channel.send("경고를 1회 받았습니다.")
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(author.id)
                sheet["B" + str(i)].value = 1
                file.save("경고.xlsx")
                await message.channel.send("경고를 1회 받았습니다.")
                break
            i += 1


client.run(NjgwMzExNTI5MzU4MjI5NjE4.Xk-Ehg.cWDSv1Z8-M8Y2ykunDPC-SQohGk)
