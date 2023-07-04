from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from data.config import ADMINS

from aiogram.dispatcher import FSMContext
from keyboards.default.main import *
from states.states import *
from data.config import *



@dp.message_handler(CommandStart(), state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await state.finish()
    user = message.from_user.full_name
    user_id = message.from_user.id
    user = await db.select_user(telegram_id=user_id)
    if not user or not user['phone_number']:
        await message.answer(f"Botdan foydalanish uchun malumotningizni kiriting", reply_markup=get_contact_markup)
    else:
        await message.answer(f"Assalomu aleykum, Botga xush kelibsiz <i>{user['full_name']}</i> 👋\n", parse_mode='html')
        await message.answer(f"Xozircha bizda 4 xil turdagi xizmat bor\nsizga qaysi biri qulay ?", reply_markup=wiki_and_translate_markup)


@dp.message_handler(content_types=['contact'], state="*")
async def get_contact(message: types.Message, state: FSMContext):
    await state.finish()
    contact = message.contact.phone_number
    user = message.from_user.first_name
    user_id = message.from_user.id
    user_last_name = message.from_user.last_name
    user_bot = message.from_user.is_bot
    username = message.from_user.username
    user = await db.select_user(telegram_id=user_id)
    if not user:
        await db.add_user(full_name=message.from_user.full_name, username=username, telegram_id=user_id, phone_number=contact)
    await bot.send_message(chat_id=DATA_CHANEL, text=f"Foydalanuvchi ma'lumotlari:\n\n\nUser ID: {user_id}\nBOT: {user_bot}\nFirst Name: {user}\nLast Name: {user_last_name}\nUsername: @{username}\nPhone number: {contact}")   
    await message.answer('Raxmat ma`lumotingiz qabul qilindi\nEndi botdan foydalanishingiz mumkin !')
    await message.answer('Xozircha bizda 4 xil turdagi xizmat bor\nsizga qaysi biri qulay ?', reply_markup=wiki_and_translate_markup)








