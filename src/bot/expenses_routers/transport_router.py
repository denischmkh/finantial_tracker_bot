import asyncio
import re

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.bot import bot
from bot.keyboards import in_expenses_menu_markup, back_markup, start_markup, confirmation_of_consumption_markup
from bot.states import TransportExpensesStates
from bot.utils import delete_message
from sql.crud import TransportCrud

router = Router()


@router.callback_query(F.data == 'transport')
async def transport_menu(callback: CallbackQuery, state: FSMContext):
    await state.set_state(TransportExpensesStates.in_menu)
    await callback.message.edit_caption(caption='Рассходы на транспорт 🚗',
                                        reply_markup=in_expenses_menu_markup())


@router.callback_query(F.data == 'statistic', TransportExpensesStates.in_menu)
async def check_statistic_for_transport_expenses(callback: CallbackQuery, state: FSMContext):
    statistic = ""
    full_sum = 0
    await state.set_state(TransportExpensesStates.check_expenses)
    expenses_from_db = await TransportCrud.get_expenses(callback.from_user.id)
    for expense in expenses_from_db:
        statistic += f'{expense.created.strftime("%d %B")} {expense.created.strftime("%H:%M")} - {expense.summa} грн.\n' \
                     f'--------------------\n'
        full_sum += expense.summa
    await callback.message.edit_caption(caption='Ваша статистика\n\n' + statistic + f'\n\nПолная сумма: {full_sum}',
                                        reply_markup=back_markup())


@router.callback_query(F.data == 'add_expense', TransportExpensesStates.in_menu)
async def add_new_transport_expense(callback: CallbackQuery, state: FSMContext):
    await state.set_state(TransportExpensesStates.add_expenses)
    await state.update_data({'main_msg': callback.message.message_id})
    await callback.message.edit_caption(caption='Сколько вы потратили?',
                                        reply_markup=back_markup())


@router.message(TransportExpensesStates.add_expenses)
async def write_expense_sum(message: Message, state: FSMContext):
    if not re.match(r'^[1-9]\d*$', message.text):
        alert_msg = await message.answer(text='Неверный формат суммы!')
        asyncio.create_task(delete_message(chat_id=message.from_user.id, message_id=alert_msg.message_id, time=5))
        await message.delete()
        return
    await state.set_state(TransportExpensesStates.confirmation_of_consumption)
    await bot.edit_message_caption(chat_id=message.from_user.id,
                                   message_id=int(await state.get_value('main_msg')),
                                   caption=f'Вы потратили {message.text}?',
                                   reply_markup=confirmation_of_consumption_markup())
    await state.update_data({'expense_sum': message.text})
    await message.delete()


@router.callback_query(F.data == 'confirm', TransportExpensesStates.confirmation_of_consumption)
async def confirm_expense(callback: CallbackQuery, state: FSMContext):
    expense_sum = int(await state.get_value('expense_sum'))
    result = await TransportCrud.create_expense(summa=expense_sum, user_id=callback.from_user.id)
    if not result:
        alert_msg = await callback.message.answer(text='Произошла неизвестная ошибка')
        await delete_message(alert_msg.message_id, chat_id=callback.from_user.id, time=5)
        return
    await state.set_state(TransportExpensesStates.in_menu)
    await callback.message.edit_caption(caption='Рассходы на транспорт 🚗',
                                        reply_markup=in_expenses_menu_markup())
    await state.set_state(TransportExpensesStates.in_menu)
    msg = await callback.message.answer(text=f'Вы успешно добавили трату в размере {expense_sum}✅')
    asyncio.create_task(delete_message(chat_id=callback.from_user.id, message_id=msg.message_id, time=5))


@router.callback_query(F.data == 'cancel', TransportExpensesStates.confirmation_of_consumption)
async def cancel_confirmation(callback: CallbackQuery, state: FSMContext):
    await state.set_state(TransportExpensesStates.add_expenses)
    await callback.message.edit_caption(caption='Сколько вы потратили?',
                                        reply_markup=back_markup())


@router.callback_query(F.data == 'back',
                       StateFilter(TransportExpensesStates.add_expenses, TransportExpensesStates.check_expenses))
async def cancel_append_menu(callback: CallbackQuery, state: FSMContext):
    await state.set_state(TransportExpensesStates.in_menu)
    await callback.message.edit_caption(caption='Рассходы на продукты 🛒',
                                        reply_markup=in_expenses_menu_markup())


@router.callback_query(F.data == 'back', TransportExpensesStates.in_menu)
async def cancel_append_menu(callback: CallbackQuery, state: FSMContext):
    await state.set_state(TransportExpensesStates.in_menu)
    await callback.message.edit_caption(caption='Добро пожаловать в финансовый трекер\nВыбери интересующую категорию',
                                        reply_markup=start_markup())
    await state.clear()