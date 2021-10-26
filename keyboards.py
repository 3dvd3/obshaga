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


makup_block = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    one_time_keyboard=True,
).row(another_markup
)



return_hard_button = KeyboardButton("Посмотреть правильный ответ✅")
makup_hard_return = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).row(return_hard_button
).row(new_defin, new_hard_quest
).row(another_markup)        


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
economic = KeyboardButton("Экономика")
politic = KeyboardButton("Политика")
pravo = KeyboardButton("Право")
randomka = KeyboardButton("Рандом")
makup_theme = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).row(human_and_obshaga, politic
).row(economic, pravo
)



deffins_economic = KeyboardButton("Определения по теме \"Экономика\"")
hards_economic = KeyboardButton("Сложные вопросы по теме \"Экономика\"")
another_markup = KeyboardButton("Выбрать другой блок.")
makup_choice_econom = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).row(deffins_economic, hards_economic
).row(another_markup)


return_button_econom = KeyboardButton("Посмотреть ответ✅")
another_markup = KeyboardButton("Выбрать другой блок.")
makup_returns = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).row(return_button_econom
).row(deffins_economic, hards_economic
).row(another_markup)

return_button_econom_hard = KeyboardButton("Посмотреть ответ ✅")
makup_returns_hard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).row(return_button_econom_hard
).row(deffins_economic, hards_economic
).row(another_markup)
