import re
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


return_button = KeyboardButton("Посмотреть правильный ответ ✅")
new_defin = KeyboardButton("Определения")
new_hard_quest = KeyboardButton("Сложные вопросы")
makup_return = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).row(return_button
).row(new_defin, new_hard_quest
)


return_hard_button = KeyboardButton("Посмотреть правильный ответ✅")
makup_hard_return = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).row(return_hard_button
).row(new_defin, new_hard_quest
)        


defin_button = KeyboardButton("Определения")
hard_quest = KeyboardButton("Сложные вопросы")
makup_begin = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).row(defin_button, hard_quest
)