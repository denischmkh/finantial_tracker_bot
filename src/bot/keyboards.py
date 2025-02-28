from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_markup():
    products = InlineKeyboardButton(text='Продукты', callback_data='products')
    transport = InlineKeyboardButton(text='Транспорт', callback_data='transport')
    other = InlineKeyboardButton(text='Прочее (Одежда, Гаджеты и т.д.)', callback_data='other')
    every_month = InlineKeyboardButton(text='Ежемесячные рассходы', callback_data='every_month')
    earnings = InlineKeyboardButton(text='Заработок', callback_data='earnings')
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [products],
        [transport],
        [other],
        [every_month],
        [earnings]
    ])
    return markup
