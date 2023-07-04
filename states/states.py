from aiogram.dispatcher.filters.state import State, StatesGroup



class WikiState(StatesGroup):
    article = State()

class ShopState(StatesGroup):
    category = State()
    products = State()
    product = State()

class Kuranstate(StatesGroup):
    sura = State()
    oyat = State()

class aboutstate(StatesGroup):
    about = State()

class reklamastate(StatesGroup):
    sorov = State()