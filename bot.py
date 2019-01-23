import json
import asyncio
import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="!")
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="!müşteri", type=2))
    print("Hazırım bro")
    print("Adım " + client.user.name)
    print("ID'm: " + client.user.id)


@client.event
async def on_member_join(member):
    await client.send_message(member, "Withet sunucusuna hoşgeldin! Eğer müşteri isen *!müşteri* yazıp rolünü tekrar alabilirsin!")

    with open("müşteriler.json", "r") as f:
            müşteriler = json.load(f)


    if member.id in müşteriler:
        rolee = discord.utils.get(member.server.roles, name="Müşteri")
        await client.add_roles(member, rolee)


    with open("müşteriler.json", "w") as f:
            json.dump(müşteriler, f)


@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.UserInputError):
        await client.send_message(ctx.message.channel, "Kullanıcı bulunamadı.")

    elif isinstance(error, commands.CommandNotFound):
        pass

    else:
        if ctx.message.channel.is_private:
            await client.send_message(ctx.message.channel, "Bu komut direkt mesajlarda kullanılamaz!")
        else:
            await client.send_message(ctx.message.channel, "Birşeyler oldu.")

            await client.send_message(discord.Object(id='516318943686688817'), "**<@378181850385874944>**,  **{}** tarafından **{}** kanalında kullanılan **{}** komutunda bir hata oluştu:  **{}**".format(ctx.message.author.mention,ctx.message.channel.name,ctx.command,error))



@client.command(pass_context=True)
async def ekle(ctx, user: discord.Member):
    author = ctx.message.author
    if "bot kontrolü" in [y.name.lower() for y in author.roles]:

        embededd = discord.Embed(
            title="Başarılı!",
            description="Kullanıcı müşteri listesine eklendi!",
            colour=discord.Colour.green()
        )
        embededd.set_footer(text="Made by The Silver#3113")

        embededded = discord.Embed(
            title="Başarısız!",
            description="Kullanıcı zaten listede.",
            colour=discord.Colour.red()
        )
        embededded.set_footer(text="Made by The Silver#3113")

        with open("müşteriler.json", "r") as f:
            müşteriler = json.load(f)

        if not user.id in müşteriler:
            müşteriler[user.id] = {}
            await client.say(embed=embededd)

            rolee = discord.utils.get(user.server.roles, name="Müşteri")
            await client.add_roles(user, rolee)

        else:
            await client.say(embed=embededded)


        with open("müşteriler.json", "w") as f:
            json.dump(müşteriler, f)


@client.command(pass_context=True)
async def satınal(ctx):
    author = ctx.message.author
    Bembed = discord.Embed(
        title="Başarılı!",
        description="Sıraya girdin.",
        colour=discord.Colour.green()
    )
    Bembed.set_footer(text="Made by The Silver#3113")

    NBembed = discord.Embed(
        title="Başarılı!",
        description="Sıradan çıktın.",
        colour=discord.Colour.green()
    )
    NBembed.set_footer(text="Made by The Silver#3113")

    with open("Sıra.json", "r") as f:
        Sıra = json.load(f)

    if not author.id in Sıra:
        Sıra[author.id] = {}
        await client.say(embed=Bembed)
    else:
        del Sıra[author.id]
        await client.say(embed=NBembed)






    with open("Sıra.json", "w") as f:
        json.dump(Sıra, f)

@client.command(pass_context=True)
async def müşteri(ctx):
        user = ctx.message.author
        author = ctx.message.author

        embededd = discord.Embed(
            title="Başarılı!",
            description="Müşteri rolü verildi!",
            colour=discord.Colour.green()
        )
        embededd.set_footer(text="Made by The Silver#3113")

        embededded = discord.Embed(
            title="Başarısız!",
            description="Sen müşteri listesinde değilsin.",
            colour=discord.Colour.red()
        )
        embededded.set_footer(text="Made by The Silver#3113")

        embededdeded = discord.Embed(
            title="Başarısız!",
            description="Sende zaten müşteri rolü var.",
            colour=discord.Colour.red()
        )
        embededdeded.set_footer(text="Made by The Silver#3113")

        with open("müşteriler.json", "r") as f:
            müşteriler = json.load(f)

        if user.id in müşteriler:
            if not "müşteri" in [y.name.lower() for y in author.roles]:

                rolee = discord.utils.get(user.server.roles, name="Müşteri")
                await client.add_roles(user, rolee)
                await client.say(embed=embededd)
            else:
                await client.say(embed=embededdeded)

        else:
            await client.say(embed=embededded)


        with open("müşteriler.json", "w") as f:
            json.dump(müşteriler, f)



@client.command(pass_context=True)
async def sil(ctx, user: discord.Member):
    author = ctx.message.author
    if "bot kontrolü" in [y.name.lower() for y in author.roles]:

        embededd = discord.Embed(
            title="Başarılı!",
            description="Kullanıcı müşteri listesinden silindi!",
            colour=discord.Colour.green()
        )
        embededd.set_footer(text="Made by The Silver#3113")

        embededded = discord.Embed(
            title="Başarısız!",
            description="Kullanıcı listede yok.",
            colour=discord.Colour.red()
        )
        embededded.set_footer(text="Made by The Silver#3113")

        with open("müşteriler.json", "r") as f:
            müşteriler = json.load(f)

        if user.id in müşteriler:
            del müşteriler[user.id]
            await client.say(embed=embededd)

            role = discord.utils.get(ctx.message.server.roles, name="Müşteri")
            await client.remove_roles(user, role)

        else:
            await client.say(embed=embededded)


        with open("müşteriler.json", "w") as f:
            json.dump(müşteriler, f)

@client.command(pass_context=True)
async def bilgi(ctx):
    Fembed = discord.Embed(
        title="Bilgi",
        description="**Sadece <@512971348826390529> Satabilir.**",
        colour=discord.Colour.blue()
    )
    Fembed.set_footer(text="Made by The Silver#3113")

    Fembed.add_field(name="Withet kaç level?",value="Withet level 6 full lua bir exploittir.",inline=False)
    Fembed.add_field(name="Withet in fiyatı?",value="Withet sadece 15 tl dir.",inline=False)
    Fembed.add_field(name="Witheti nerden alabilirim?",value="Witheti almak için **!satınal** yazarak sıraya girebilirsiniz.    ‍      ‍      ‍      ‍    ‍       ‍       ‍       ‍       ‍       ‍       ‍       ‍       ‍       ‍       ‍       ‍       ‍       ‍          ‍   *Sıranız geldiğinde sizinle iletişime geçilecektir.*",inline=False)
    Fembed.add_field(name="Withet ile yardıma ihtiyacım var.",value="7/24 arıza ve problem durumunda desteğinize yanıt verecek kadromuz mevcuttur.",inline=False)
    Fembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/516174640390078475/516305222717669376/wtlogo_icon.png")


    await client.say(embed=Fembed)


@client.command(pass_context=True)
async def sıra(ctx):
    author = ctx.message.author
    if "bot kontrolü" in [y.name.lower() for y in author.roles]:
        sexer = 1
        for server in client.servers:
            for member in server.members:
                sexer += 1

        await client.say("sunucuda {} kişi var".format(sexer))

        embeded = discord.Embed(
            title="Sıra;",
            description="",
            colour=discord.Colour.blue()
        )
        embeded.set_footer(text="Made by The Silver#3113")

        embededd = discord.Embed(
            title="Sıra;",
            description="",
            colour=discord.Colour.blue()
        )
        embededd.set_footer(text="Made by The Silver#3113")

        embededdd = discord.Embed(
            title="Sıra;",
            description="",
            colour=discord.Colour.blue()
        )
        embededdd.set_footer(text="Made by The Silver#3113")

        with open("Sıra.json", "r") as f:
            Sıra = json.load(f)

            sayar = 0

            for member.id in Sıra:
                sayar += 1
                if sayar <= 25:
                    embeded.add_field(name="{}.".format(sayar), value="<@{}>".format(member.id), inline=False)
                elif sayar <= 50:
                    embededd.add_field(name="{}.".format(sayar), value="<@{}>".format(member.id), inline=False)
                elif sayar <= 75:
                    embededdd.add_field(name="{}.".format(sayar), value="<@{}>".format(member.id), inline=False)

            await client.say(embed=embeded)
            if sayar >= 25:
                await client.say(embed=embededd)
                if sayar >= 50:
                    await client.say(embed=embededdd)

        with open("Sıra.json", "w") as f:
            json.dump(Sıra, f)



@client.command(pass_context=True)
async def liste(ctx):
    author = ctx.message.author
    if "bot kontrolü" in [y.name.lower() for y in author.roles]:
        sexer = 1
        for server in client.servers:
            for member in server.members:
                sexer += 1

        await client.say("sunucuda {} kişi var".format(sexer))

        embeded = discord.Embed(
            title="Müşteri listesi;",
            description="",
            colour=discord.Colour.blue()
        )
        embeded.set_footer(text="Made by The Silver#3113")

        embededd = discord.Embed(
            title="Müşteri listesi;",
            description="",
            colour=discord.Colour.blue()
        )
        embededd.set_footer(text="Made by The Silver#3113")

        embededdd = discord.Embed(
            title="Müşteri listesi;",
            description="",
            colour=discord.Colour.blue()
        )
        embededdd.set_footer(text="Made by The Silver#3113")

        with open("müşteriler.json", "r") as f:
            müşteriler = json.load(f)

            sayar = 0

            for member.id in müşteriler:
                sayar += 1
                if sayar <= 25:
                    embeded.add_field(name="{}.".format(sayar), value="<@{}>".format(member.id), inline=False)
                elif sayar <= 50:
                    embededd.add_field(name="{}.".format(sayar), value="<@{}>".format(member.id), inline=False)
                elif sayar <= 75:
                    embededdd.add_field(name="{}.".format(sayar), value="<@{}>".format(member.id), inline=False)

            await client.say(embed=embeded)
            if sayar >= 25:
                await client.say(embed=embededd)
                if sayar >= 50:
                    await client.say(embed=embededdd)

        with open("müşteriler.json", "w") as f:
            json.dump(müşteriler, f)



  
  
 
#YOU CAN USE os.environ TO HIDE YOUR BOT TOKEN: SAVE YOUR BOT TOKEN AS THE NAME YOU GAVE IN os.environ['name'] 
bot.run(os.environ['token'])
