import asyncio
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
import pandas as pd

@dp.message_handler(text='/countusers', user_id = ADMINS, state="*")
async def count_users(message: types.Message):
    count_users = await db.count_users()
    await message.answer(text=f'Foydalanuvchilar soni: {count_users}')

@dp.message_handler(text="/allusers", user_id=ADMINS, state="*")
async def get_all_users(message: types.Message):
    users = await db.select_all_users()
    id = []
    name = []
    for user in users:
        id.append(user[-2])
        name.append(user[1])
    data = {
        "Telegram ID": id,
        "Name": name
    }
    pd.options.display.max_rows = 10000
    df = pd.DataFrame(data)
    if len(df) > 50:
        for x in range(0, len(df), 50):
            await bot.send_message(message.chat.id, df[x:x + 50])
    else:
       await bot.send_message(message.chat.id, df)
       

# @dp.message_handler(text="/reklama", user_id=ADMINS)
# async def send_ad_to_all(message: types.Message):
  

@dp.message_handler(text="/cleandb", user_id=ADMINS, state="*")
async def get_all_users(message: types.Message):
    await db.delete_users()
    await message.answer("Baza tozalandi!")





@dp.message_handler(commands=['info_bot'], state="*")
async def do_help(message: types.Message):
    await message.reply(text=f"""Bu bot hozirda 4 xil fazifa bajara oladi 

Bular : 

1 - Dunyodagi yirik ma\'lumotlar bazasi Wikipedia dan ma\'lumot qidirib bera oladi,

2 - Siz hohlagan tildagi matnlarni hohlagan tilga tarjima qilib bera oladi (Tarjimon) 

3 - Ushbu bot sizga online do\'kon mahsulotlarini taklif eta oladi

4 - Bu bot orqali siz Muqaddas Qur\'oni Karimdan barcha oyatlarni o\'zbek tilida o\'qish imkoniyatiga ega bo\'lasiz.

Bu bot yaratilgan sana : 04.07.2023""")