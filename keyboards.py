import re
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


return_button = KeyboardButton("Посмотреть правильный ответ ✅")
new_defin = KeyboardButton("Определения по теме \"Человек и общество\"")
new_hard_quest = KeyboardButton("Сложные вопросы по теме \"Человек и общество\"")
another_markup = KeyboardButton("Выбрать другой блок.")
makup_return = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).row(return_button
).row(new_defin, new_hard_quest
).row(another_markup)


return_hard_button = KeyboardButton("Посмотреть правильный ответ✅")
makup_hard_return = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).row(return_hard_button
).row(new_defin, new_hard_quest
)        


defin_button = KeyboardButton("Определения по теме \"Человек и общество\"")
hard_quest = KeyboardButton("Сложные вопросы по теме \"Человек и общество\"")
another_markup = KeyboardButton("Выбрать другой блок.")
makup_begin = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).row(defin_button, hard_quest
).row(another_markup
)
makup_begin_human = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).row(defin_button, hard_quest)




human_and_obshaga = KeyboardButton("Человек и общество")
makup_theme = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).row(human_and_obshaga
)


