from loader import db, dp
from aiogram import types
from states.states import WikiState, ShopState, aboutstate, Kuranstate, reklamastate
from keyboards.default.main import wiki_and_translate_markup, geturl, datainfo, name_product, kuron
from aiogram.dispatcher import FSMContext

@dp.message_handler(text = "🏠 Asosiy Menu", state="*")
@dp.message_handler(text = "⬅️ Orqaga", state=WikiState.article)
async def main_menu_redirect_wiki(message: types.Message, state: FSMContext):
    await message.answer('Siz asosiy Menudasiz\n\niltimos kerakli xizmatni tanlang !', reply_markup=wiki_and_translate_markup)
    await state.finish()

@dp.message_handler(text = "⬅️ Orqaga", state=ShopState.category)
async def main_menu_redirect_shop(message: types.Message, state: FSMContext):
    await message.answer('Siz asosiy Menudasiz\n\niltimos kerakli xizmatni tanlang !', reply_markup=wiki_and_translate_markup)
    await state.finish()


@dp.message_handler(text = "⬅️ Orqaga", state=ShopState.products)
async def category_redirect_shop(message: types.Message):
    markup = geturl()[0]
    await message.answer('Qaysi Kategoriya kerak ?', reply_markup= markup)
    await ShopState.category.set()


@dp.message_handler(text="⬅️ Orqaga", state=aboutstate.about)
async def back(message: types.Message, state: FSMContext):
    await message.answer("Siz asosiy Menudasiz\n\niltimos kerakli xizmatni tanlang !", reply_markup=wiki_and_translate_markup)
    await state.finish()



@dp.message_handler(text = "🏠 Asosiy Menu", state="*")
async def main_menu_redirect(message: types.Message, state: FSMContext):
    await message.answer('Siz asosiy Menudasiz\n\niltimos kerakli xizmatni tanlang !', reply_markup=wiki_and_translate_markup)
    await state.finish()



@dp.message_handler(text = "⬅️ Orqaga", state=Kuranstate.sura)
async def main_redirect_kuran(message: types.Message, state: FSMContext):
    await message.answer('Siz asosiy Menudasiz\n\niltimos kerakli xizmatni tanlang !', reply_markup=wiki_and_translate_markup)
    await state.finish()


@dp.message_handler(text = "⬅️ Orqaga", state=Kuranstate.oyat)
async def sura_redirect_kuran(message: types.Message):
    await message.answer("Qaysi suraning oyati kerak ?", reply_markup=kuron())
    await Kuranstate.sura.set()


@dp.message_handler(text = "⬅️ Orqaga", state=reklamastate.sorov)
async def main_redirect_add(message: types.Message, state: FSMContext):
    await message.answer("Siz asosiy Menudasiz\n\niltimos kerakli xizmatni tanlang !", reply_markup=wiki_and_translate_markup)
    await state.finish()