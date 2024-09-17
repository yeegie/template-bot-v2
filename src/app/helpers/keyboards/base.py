from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton, InlineKeyboardBuilder, InlineKeyboardButton
from app.helpers.fabric.base import BaseCallback


def keyboard():
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text='Button 1'))

    return builder.as_markup(resize_keyboard=True)


def inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="Button 1",
            callback_data=BaseCallback(action="action1", value="1sW7:12").pack()
        )
    )

    return builder.as_markup(resize_keyboard=True)
