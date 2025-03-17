import discord
from discord.ext import commands
from discord import app_commands
import os

TOKEN = "MTM1MTEzMjAzMTI5MTIyODE3MA.GYtMlY.mLiFXOnSZN77CT1vUl47y4txPqcPJju_8Z0HK4"
GUILD_ID = 1218967861578563584  # Thay bằng ID server Discord của bạn

# Khởi tạo bot với intents
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree

# Dữ liệu nhân vật lưu trong mã (dictionary)
characters = {
    "naruto": "Nhẫn giả làng Lá, có Cửu Vĩ Hồ Ly.",
    "sasuke": "Nhẫn giả Uchiha, sở hữu Sharingan.",
    "sakura": "Thành viên Đội 7, có sức mạnh y thuật.",
    "kakashi": "Thầy của Đội 7, sở hữu Sharingan một mắt."
}


@bot.event
async def on_ready():
    try:
        guild = discord.Object(id=GUILD_ID)
        bot.tree.clear_commands(guild=guild)
        await bot.tree.sync(guild=None)

        print(f"Bot đã đăng nhập thành công với {bot.user}")
        print("Lệnh đã được đồng bộ lại!")
    except Exception as e:
        print(f"Lỗi đồng bộ lệnh: {e}")


@bot.event
async def on_ready():
    print(f"Đã đăng nhập với {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Đã đồng bộ {len(synced)} lệnh slash!")
    except Exception as e:
        print(f"Lỗi khi đồng bộ lệnh: {e}")

@tree.command(name="res", description="Resonance Plan")
async def res(interaction: discord.Interaction, name: str):
    name = name.lower()  # Chuyển thành chữ thường
    if name in characters:
        await interaction.response.send_message(characters[name])
    else:
        await interaction.response.send_message("Không tìm thấy nhân vật!")


# Chạy bot trên Replit với token từ Biến môi trường
bot.run(TOKEN)
