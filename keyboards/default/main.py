from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, WebAppInfo

import requests




#WebAPPS
web_app = WebAppInfo(url = 'https://translate.google.com/')







#Buttons 
main = KeyboardButton(text="🏠 Asosiy Menu")
back_button = KeyboardButton(text='⬅️ Orqaga')
about_btn = KeyboardButton("✍️ Taklif va Shikoyatlar")
kuran = KeyboardButton("Qur`oni Karim")
data_malumot_button= KeyboardButton(text='Online Shop')
translate_button = KeyboardButton(text='Translater xizmati', web_app=web_app)
wikipedia_button = KeyboardButton(text= 'Wikipediya xizmati')
tekshirish_button = KeyboardButton("Tekshirish")






#default keyboards
markup_back = ReplyKeyboardMarkup(resize_keyboard=True)
markup_back.add(back_button, main)


mainbutton = ReplyKeyboardMarkup(resize_keyboard=True)
mainbutton.add(main)


wiki_and_translate_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
wiki_and_translate_markup.add(wikipedia_button, translate_button, data_malumot_button, kuran, about_btn)



tekshirish_markup = ReplyKeyboardMarkup(resize_keyboard=True)
tekshirish_markup.add(tekshirish_button)


get_contact_markup = ReplyKeyboardMarkup(resize_keyboard=True)
contact_button = KeyboardButton("Telefon Raqamni ulashish",request_contact=True)
get_contact_markup.add(contact_button)

# Inline Keyboards











#DEFAULT FUNCTIONS

def geturl():
    url = 'https://dummyjson.com/products/categories'
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
    response = requests.get(url=url).json()
    for info in response:
        markup.insert(KeyboardButton(text=info.title()))
    markup.add(back_button, main)
    return markup, response



def datainfo(category):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
    url = f'https://dummyjson.com/products/category/{category}'
    response = requests.get(url=url).json()
    products = response['products']
    product_titles = []
    for product in products:
        markup.insert(KeyboardButton(text=product.get("title")))
        product_titles.append(product.get('title'))
    markup.add(back_button, main)
    return markup, product_titles




def name_product(title):
    url = f'https://dummyjson.com/products/search?q={title}'
    response = requests.get(url=url).json()
    products = response['products']
   
    product_info = []
    for product in products:
        product_info.append(product)
    
    for info in product_info:
        prod_info = f"Name: {info.get('title')}\n\nDescription: {info.get('description')}\n\nPrice: {info.get('price')}$"
        prod_photo = info.get('thumbnail')
    return prod_info, prod_photo



def kuron():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/info.json"
    response = requests.get(url=url).json()
    chapters = response['chapters']
    for name in chapters:
        markup.insert(KeyboardButton(text=f'{name["chapter"]}.{name["name"]}'))
    markup.add(back_button, main)
    return markup



def get_vers(chap):
    url = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu.json"
    response2 = requests.get(url=url).json()
    curan = response2['quran']
    verse_len = []
    for oyat in curan:
        if oyat['chapter'] ==  int(chap):
            verse_len.append(oyat["verse"])
    return verse_len



def get_chapter(sura_name):
    url ="https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/info.json"
    response = requests.get(url=url).json()
    chapters = response['chapters']
    chap = ''
    for name in chapters:
        if name['name'] ==  sura_name:
            chap += str(name['chapter'])
    return chap
