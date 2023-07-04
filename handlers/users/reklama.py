import asyncio
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
import pandas as pd
from keyboards.default.main import *
from aiogram.dispatcher import FSMContext
from states.states import *


@dp.message_handler(text="/reklama", user_id=ADMINS, state="*")
async def ask_add(message: types.Message):
    await message.answer("Reklama bo`limiga hush kelibsiz", reply_markup=ReplyKeyboardRemove())
    await message.answer("Reklama sifatida yubormoqchgi bolgan matningizni kiriting\nva bu matn bu botni barcha foydalanuvchilariga boradi\nshunday ekan reklamani xatosiz ekaniga ishonch hosil qiling !", reply_markup=markup_back)
    await reklamastate.sorov.set()


@dp.message_handler(state=reklamastate.sorov)
async def send_ad_to_all(message: types.Message, state: FSMContext):
    users = await db.select_all_users()
    try: 
        for user in users:
            user_id = user[-2]
            await bot.send_message(chat_id=user_id, text=message.text)
            await asyncio.sleep(0.05)
        await message.answer("Reklama muvofaqiyatli tarqatildi", reply_markup=ReplyKeyboardRemove() and wiki_and_translate_markup)
        await state.finish()
    except:
        await bot.send_message(chat_id=ADMINS, text="Reklama tarqatishda xatolik !")
        await state.finish()