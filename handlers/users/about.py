import asyncio
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
import pandas as pd
from states.states import aboutstate 
from aiogram.dispatcher import FSMContext
from keyboards.default.main import *
from data.config import CHANNEL_TAKLIF
from handlers.users.back import back


@dp.message_handler(text ='✍️ Taklif va Shikoyatlar')
async def about(message: types.Message):
    await message.answer(text="Taklif yoki shikoyatingizni yozing 👇", reply_markup= ReplyKeyboardRemove())
    await message.answer(text="Taklif yoki shikoyatingiz Anonim korinishida Bo`ladi", reply_markup= markup_back)
    await aboutstate.about.set()


@dp.message_handler(state= aboutstate.about)
async def send_msg(message: types.Message, state: FSMContext):
    user = message.from_user.full_name
    username = message.from_user.username
    await bot.send_message(chat_id=CHANNEL_TAKLIF, text=f'NAME :  {user}\nUSERNAME :  @{username}\n\nBu foydlanuvchi yuborgan Taklif/Shkoyat 👇\n**************************************\n\n<i> {message.text} </i>\n\n**************************************', parse_mode='html')
    await message.answer("Taklif yoki shikoyatingiz qabul qilindi\nYordamingiz uchun raxmat 🫡", reply_markup= wiki_and_translate_markup)
    await state.finish()

   
    


