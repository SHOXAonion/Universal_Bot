
from aiogram import types
from keyboards.default.main import name_product, geturl, datainfo
from states.states import ShopState
from app import db, dp
from aiogram.dispatcher import FSMContext





@dp.message_handler(text = 'Online Shop')
async def data_malumott(message: types.Message):
    markup = geturl()[0]
    await message.answer('Qaysi Kategoriya kerak ?', reply_markup= markup)
    await ShopState.category.set()


@dp.message_handler(lambda message: message.text.lower() in geturl()[1], state=ShopState.category)
async def get_products(message: types.Message):
    category = message.text.lower()
    data = datainfo(category=category)
    await message.answer("Mahsulotni tanlang", reply_markup=data[0])
    await ShopState.products.set()

@dp.message_handler(state=ShopState.products)
async def get_product(message: types.Message):
    try:
        product_info = name_product(title= message.text)
        await message.answer_photo(photo=f"{product_info[1]}",caption=f"{product_info[0]}") 
    except:
        await message.answer("Bunday Mahsulot Hali mavjud emas !\niltimos boshqa mahsulot qarab ko`ring !")
    



