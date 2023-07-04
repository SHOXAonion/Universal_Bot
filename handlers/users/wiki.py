from aiogram import types

from states.states import WikiState, ShopState
import wikipedia

from app import db, dp
from aiogram.dispatcher import FSMContext
from keyboards.default.main import markup_back, wiki_and_translate_markup


wikipedia.set_lang('uz')

@dp.message_handler(text='Wikipediya xizmati')
async def wikipedia_xizmat(message: types.Message, state: FSMContext):
    await message.answer('Wikipedia xizmatiga xush kelibsiz !\nsizga qanday malumot kerak bo`lsa yozing', reply_markup=types.ReplyKeyboardRemove())
    await message.answer('Men uni sizga wikipedia dan qidirib beraman', reply_markup=wiki_and_translate_markup and markup_back)
    await WikiState.article.set()

@dp.message_handler(state=WikiState.article)
async def send_wiki(message: types.Message):
    msg = await message.answer("Iltimos Kuting...🔍")
    try:
        response = wikipedia.summary(message.text)  
        await message.answer(response)
        await msg.delete()
    except:
        await message.answer('Bu mavzuga oid maqola topilmadi !!!\niltimos boshqa biror narsa qidirib ko`ring')
    

