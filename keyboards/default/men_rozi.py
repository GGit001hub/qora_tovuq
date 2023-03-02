from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

men_rizo = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Men o'ynashga roziman",request_location=True)
        ]
    ],
    resize_keyboard=True,one_time_keyboard=True
)
