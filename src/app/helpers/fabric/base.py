from aiogram.filters.callback_data import CallbackData


class BaseCallback(CallbackData, prefix='cb'):
    action: str
    value: str
