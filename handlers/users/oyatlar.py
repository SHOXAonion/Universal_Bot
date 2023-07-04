from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from data.config import ADMINS

from aiogram.dispatcher import FSMContext
from keyboards.default.main import *
from states.states import *
from data.config import *



@dp.message_handler(text = "Qur`oni Karim")
async def oyat(message: types.Message):
    await message.answer("Qaysi suraning oyati kerak ?", reply_markup=kuron())
    await Kuranstate.sura.set()




@dp.message_handler(state=Kuranstate.sura)
async def suralar(message: types.Message, state: FSMContext):
    sura_name = message.text.split('.')
    sura_name = sura_name[-1]
    chapter = get_chapter(sura_name=sura_name)
    vers_len = get_vers(chap=chapter)
    await message.answer(f" {sura_name} surasi {vers_len[-1]} ta oyatdan iborat\n\n O`qimoqchi bo`lgan oyatingizni raqamini kiriting !",reply_markup= types.ReplyKeyboardRemove())
    await message.answer("Men bu oyatni sizga uzbekchasini taqdim etaman !", reply_markup=markup_back)
    await state.update_data({"sura_name":sura_name})
    await state.update_data({"chapter":chapter})
    await state.update_data({"vers_len":vers_len})
    await Kuranstate.oyat.set()



@dp.message_handler(state=Kuranstate.oyat)
async def oyatlar(message: types.Message, state: FSMContext):
    data = await state.get_data()
    sura_name = data['sura_name']
    chapter = data['chapter']
    vers_len = data['vers_len']
    try:
        if int(message.text) <= int(vers_len[-1]):
            r = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu.json").json()
            for i in r['quran']:
                if i['chapter'] == int(chapter):
                    if i['verse'] == int(message.text):
                        sms = f'<b>{sura_name} surasi {message.text}-oyat</b>\n\n'
                        sms += f"{i['text']}"
                        await message.answer(sms, reply_markup= markup_back)
        else:
            await message.answer(f"{sura_name} surasida {vers_len[-1]} ta oyat mavjud !\niltimos raqamni tekshirib qaytadan kiriting !")
    except:
        await message.answer("Iltimos so\'rovni to\'g\'ri kiriting !")        