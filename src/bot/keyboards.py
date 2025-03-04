from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_markup():
    products = InlineKeyboardButton(text='Продукты 🛒', callback_data='products')
    transport = InlineKeyboardButton(text='Транспорт 🚗', callback_data='transport')
    other = InlineKeyboardButton(text='Прочее (Одежда, Гаджеты и т.д.) 👚📱', callback_data='other')
    every_month = InlineKeyboardButton(text='Ежемесячные расходы 📅', callback_data='every_month')
    earnings = InlineKeyboardButton(text='Заработок 💰', callback_data='earnings')
    statistic = InlineKeyboardButton(text='Статистика за прошлые месяцы 📊', callback_data='statistic')
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [products],
        [transport],
        [other],
        [every_month],
        [earnings],
        [statistic]
    ])
    return markup


def back_markup():
    back = InlineKeyboardButton(text='Назад ↩️', callback_data='back')
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [back]
    ])
    return markup


def products_markup():
    statistic = InlineKeyboardButton(text='Статистика за текущий месяц 📊', callback_data='statistic')
    add_expense = InlineKeyboardButton(text='Добавить трату ➕', callback_data='add_expense')
    back = InlineKeyboardButton(text='Назад ↩️', callback_data='back')
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [add_expense],
        [statistic],
        [back]
    ])
    return markup


def confirmation_of_consumption_markup():
    confirm = InlineKeyboardButton(text='Подтвердить ✅', callback_data='confirm')
    cancel = InlineKeyboardButton(text='Отмена ❌', callback_data='cancel')
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [confirm, cancel],
    ])
    return markup