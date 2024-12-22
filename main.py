from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

# Cargar variables de entorno desde el archivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Crear los intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Crear el bot con el prefix y los intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento cuando el bot se conecta correctamente
@bot.event
async def on_ready():
    print(f"Conectado como: {bot.user}")
    print(f"ID del bot: {bot.user.id}")

# Contestación a ciertos mensajes
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == 'panel':
        await message.channel.send('**Funciones Activas**:\n'
                                   '**Aimbot**\n'
                                   '**Target: Head, Neck, Drag**\n\n'
                                   '**Aimfov Sniper**\n'
                                   '**Quick Sniper**\n'
                                   '**Scope Sniper**\n\n'
                                   '**Speed Timer (With Reset)**\n'
                                   '**Wall Hack Matrix**\n'
                                   '**Camara Pro (Derecha)**\n\n'
                                   '**Fix**\n'
                                   '**Chams**\n\n'
                                   '**Bypass Emulator (P64/N32)**')

    elif message.content.lower() == 'booster':
        await message.channel.send('𝐄𝐬𝐭𝐨𝐬 𝐬𝐨𝐧 𝐥𝐨𝐬 𝐩𝐫𝐞𝐦𝐢𝐨𝐬 𝐪𝐮𝐞 𝐫𝐞𝐜𝐢𝐛𝐢𝐫𝐚́𝐬 𝐩𝐨𝐫 𝐁𝐨𝐨𝐬𝐭𝐞𝐚𝐫 𝐞𝐥 𝐬𝐞𝐫𝐯𝐢𝐝𝐨𝐫:\n'
                                   '𝟐 𝐁𝐨𝐨𝐬𝐭 -> 𝟏𝟎 𝐝𝐢́𝐚𝐬 𝐝𝐞 𝐏𝐚𝐧𝐞𝐥\n'
                                   '𝟒 𝐁𝐨𝐨𝐬𝐭 -> 𝟐𝟎 𝐝𝐢́𝐚𝐬 𝐝𝐞 𝐏𝐚𝐧𝐞𝐥\n'
                                   '𝟔 𝐁𝐨𝐨𝐬𝐭 -> 𝟒𝟎 𝐝𝐢́𝐚𝐬 𝐝𝐞 𝐏𝐚𝐧𝐞𝐥')
    await bot.process_commands(message)

# Comando "nuevoembed"
@bot.command()
async def nuevoembed(ctx):
    embed = discord.Embed(
        title="𝐒𝐀𝐎 𝐇𝐀𝐂𝐊",
        description="""🇲🇽 Este software está diseñado para proporcionar a sus usuarios funciones completamente seguras y sin restricciones en los modos de juego, ofreciendo todas las características disponibles.
    ★════◈◈◈════★
         **Funciones Del Panel**
    ──➢**Aimbot**
    ──➢**Target: Head, Neck, Drag**
    ──➢**Aimfov Sniper**
    ──➢**Quick Sniper**
    ──➢**Scope Sniper**
    ──➢**Speed Timer (With Reset)**
    ──➢**Wall Hack Matrix**
    ──➢**Camara Pro (Derecha)**
    ──➢**Fix**
    ──➢**Chams**
    ──➢**Bypass Emulator (P64/N32)**
    """,
        color=discord.Color.dark_gray()
    )
    embed.add_field(name="★════◈◈◈════★", value="**𝙇𝙖𝙨 𝙢𝙚𝙟𝙤𝙧𝙚𝙨 𝙛𝙪𝙣𝙘𝙞𝙤𝙣𝙚𝙨**", inline=True)
    embed.set_author(name='𝓥𝓐𝓜𝓟𝓘𝓡𝓔')
    embed.set_thumbnail(url="https://i.pinimg.com/736x/82/b6/c9/82b6c90d3c9ecc8ff4968f6d5adb43b4.jpg")
    embed.set_image(url="https://i.pinimg.com/736x/30/c8/79/30c8795e1829682dbc32cbffbc19ac57.jpg")
    embed.set_footer(text="**DEV - Haeasy**")

    await ctx.send(embed=embed)

# Comando "nuevoembed2"
@bot.command()
async def nuevoembed2(ctx):
    embed2 = discord.Embed(
        title="𝙍𝙚𝙜𝙡𝙖𝙨 𝙎𝘼𝙊 𝙃𝘼𝘾𝙆",
        description="""  ➤ **Sé respetuoso** con todos los miembros.
    ➤ **No usar lenguaje inapropiado** en el chat.
    ➤ **No hacer spam** de ningún tipo.
    ➤ **Prohibido el material pornográfico/adulto/NSFW** o cualquier otro tipo de contenido inapropiado.
    ➤ **No se admiten anuncios de servidores ajenos** o externos.
    ➤ **No se permiten nombres ni fotos de perfil ofensivos**.
    ➤ **No está permitido realizar amenazas**, ya sean directas o indirectas.
    ➤ **Evitar menciones innecesarias**; puede ser molesto para otros usuarios.
    ➤ **No enviar publicidad mediante mensajes directos** a otros miembros. Si se te reporta, serás baneado.
    ➤ **Prohibido el uso de multicuentas** para evadir muteos o baneos.

    **¡Cumple con las reglas para evitar problemas!**""",
        color=discord.Color.dark_gray()
    )
    embed2.add_field(name="⫘⫘⫘⫘⫘⫘⫘⫘⫘", value="**Evitar ser baneado**", inline=True)
    embed2.set_author(name='𝓥𝓐𝓜𝓟𝓘𝓡𝓔')
    embed2.set_thumbnail(url="https://i.pinimg.com/736x/66/83/ed/6683ed7f1d9d99a56d3065218c1755b9.jpg")
    embed2.set_image(url="https://i.pinimg.com/736x/ba/df/e2/badfe2ee9386abde767a72a533cbffe6.jpg")
    embed2.set_footer(text="**DEV - Haeasy**")

    await ctx.send(embed=embed2)

@bot.event
async def on_member_join(member):
    if member.bot:
        return  # No da la bienvenida a otros bots
    channel_id = 1279541276844359866  # Reemplaza este número con el ID real del canal
    channel = bot.get_channel(channel_id)
    if channel:
        embed = discord.Embed(
            title="¡Bienvenido a 𝙎𝘼𝙊 𝙃𝘼𝘾𝙆!",
            description=f"¡Hola {member.mention}, bienvenido/a a **{member.guild.name}**! \n\n"
                        "**TE GARANTIZAMOS SEGURIDAD Y CONFIANZA. Si deseas adquirir alguno de nuestros productos, visita nuestra tienda.**",
            color=discord.Color.dark_grey()
        )
        embed.add_field(
            name="🟢 **Panel-PC**",
            value="Consulta todo lo relacionado con el Panel-PC.",
            inline=False
        )
        embed.add_field(
            name="💳 **Métodos de Pago**",
            value="Aquí puedes ver los métodos de pago disponibles.",
            inline=False
        )
        embed.add_field(
            name="📤 **Ticket-SAO-HACK**",
            value="Si necesitas ayuda, abre un ticket en el canal correspondiente.",
            inline=False
        )
        embed.add_field(
            name="📜 **Reglas del Servidor**",
            value="Por favor, revisa el canal de **#reglas** para conocer las normas del servidor.",
            inline=False
        )
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text="¡Esperamos que disfrutes tu estancia!")
        embed.set_image(url="https://i.pinimg.com/736x/60/b5/e1/60b5e11ca49896a30055cf90188c04cf.jpg")
        await channel.send(embed=embed)

bot.run(TOKEN)
