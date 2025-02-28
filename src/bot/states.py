from aiogram.fsm.state import StatesGroup, State


class ProductExpensesStates(StatesGroup):
    in_menu = State()
    check_expenses = State()
    add_expenses = State()

class TransportExpensesStates(StatesGroup):
    in_menu = State()
    check_expenses = State()
    add_expenses = State()

class EveryMounthExpensesStates(StatesGroup):
    in_menu = State()
    check_expenses = State()
    add_expenses = State()

class OtherExpensesStates(StatesGroup):
    in_menu = State()
    check_expenses = State()
    add_expenses = State()


class EarningStates(StatesGroup):
    in_menu = State()
    check_earning = State()
    add_earning = State()