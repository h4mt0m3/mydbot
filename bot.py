import discord
import pandas as pd  # Dùng để đọc Excel
from discord.ext import commands
from discord import app_commands

TOKEN = "MTM1MTEzMjAzMTI5MTIyODE3MA.GYtMlY.mLiFXOnSZN77CT1vUl47y4txPqcPJju_8Z0HK4"
GUILD_ID = 1218967861578563584  # Thay bằng ID server Discord của bạn

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree  # Để đăng ký lệnh slash

# Hàm đọc dữ liệu từ Excel
def load_characters_from_excel():
    try:
        df = pd.read_excel("ResonancePlan.xlsx")  # Đọc file Excel
        characters = {}
        for _, row in df.iterrows():
            name = str(row[0]).strip().lower()  # Lấy tên từ cột A
            description = str(row[1]).strip()   # Lấy mô tả từ cột B
            characters[name] = description
        return characters
    except Exception as e:
        print(f"Lỗi khi đọc file Excel: {e}")
        return {}


@bot.event
async def on_ready():
    try:
        guild = discord.Object(id=GUILD_ID)
        bot.tree.clear_commands(guild=guild)
        await bot.tree.sync(guild=guild)

        print(f"Bot đã đăng nhập thành công với {bot.user}")
        print("Lệnh đã được đồng bộ lại!")
    except Exception as e:
        print(f"Lỗi đồng bộ lệnh: {e}")

@tree.command(name="res", description="Tra cứu nhân vật từ Excel")
async def res(interaction: discord.Interaction, character: str):
    characters = load_characters_from_excel()  # Tải dữ liệu mỗi lần gọi
    response = characters.get(character.lower(), "Không tìm thấy nhân vật này!")
    await interaction.response.send_message(response)

bot.run(TOKEN)
