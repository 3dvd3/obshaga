import logging
import random
from typing import Final
from aiogram.types import message
from aiogram.types.reply_keyboard import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import keyboards as kb

from aiogram import Bot, types # импорт типов
from aiogram.dispatcher import Dispatcher # это просто надо смирись
from aiogram.utils import executor

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from config import BOT_TOKEN

from questions_human import definitions
from questions_human import harder

from questions_economy import deffi
from questions_economy import hards

bot = Bot(token = BOT_TOKEN)

dp = Dispatcher(bot)

logging.basicConfig(level=logging.ERROR)



# default commands
@dp.message_handler(commands = "start")
async def start(message: types.Message):
    await bot.send_message(message.chat.id, text = "Привет, я бот для подготовки к ЕГЭ по обществознанию!\n\nДля начала выберите блок задании⬇.\nИ ознакомьтесь с правилами /help", reply_markup=kb.makup_theme)
    file = r"C:\Users\Totosa\Desktop\obshaga\NameID.txt"
    k = message.from_user.id
    name = message.from_user.username
    c = open(file, "a+", encoding='utf-8')
    c.write("Username: " + str(name) + ";" + " ID: " + str(k) + "\n")
    c.close
    uniqlines = set(open(file,'r', encoding='utf-8').readlines())
    gotovo = open(file,'w', encoding='utf-8').writelines(set(uniqlines))


@dp.message_handler(commands = "help")
async def help(message: types.Message):
    await bot.send_message(message.chat.id, text = "Управление ботом осущетсвляется при помощи меню снизу⬇.\n\nОтветы на вопросы необходимо просто написать в чат.\nПриятного обучения.✨")



@dp.message_handler(commands = "voices")
async def ege(message: types.Message):
    file = r"C:\Users\Totosa\Desktop\obshaga\int.mp3"
    c = open(file, "rb")
    await bot.send_voice(message.chat.id, c)




@dp.message_handler(commands = "users")
async def info(message: types.Message):
    fille = r"C:\Users\Totosa\Desktop\obshaga\int.mp3"
    k = open(fille, "r", encoding="UTF-8")
    contents = k.readlines()
    c = "".join(contents)
    await message.reply("Все, кто писал боту:\n" + str(c))
# default commands

# keyboards reply
@dp.message_handler(lambda message: message.text == "Выбрать другой блок.")
async def button_new_another(message: types.Message):
    file = r"C:\Users\Totosa\Desktop\obshaga\NameID.txt"
    k = message.from_user.id
    name = message.from_user.username
    c = open(file, "a+", encoding='utf-8')
    c.write("Username: " + str(name) + ";" + " ID: " + str(k) + "\n")
    c.close
    uniqlines = set(open(file,'r', encoding='utf-8').readlines())
    gotovo = open(file,'w', encoding='utf-8').writelines(set(uniqlines))
    await bot.send_message(message.chat.id, text = "Выберите блок.\n\n*в дальнейшем пополню*", reply_markup=kb.makup_theme)


@dp.message_handler(lambda message: message.text == "Человек и общество")
async def button_theme(message: types.Message):
    await bot.send_message(
    message.chat.id, text = "Вы выбрали тему: Человек и общество\n\nВыберите вопросы по этой теме.",
    reply_markup=kb.makup_begin)


@dp.message_handler(lambda message: message.text == "Определения по теме \"Человек и общество\"")
async def button_defin(message: types.Message):
    global word
    global word_next
    global defin
    global mode
    mode = 1
    defin = random.choice(definitions)
    word = defin.split("-")
    sasuke = word[1]
    word_next = sasuke.strip()
    ze_waaardo = word[0]
    print(str(ze_waaardo) + "это...")
    print(str(defin))
    await bot.send_message(message.chat.id, text = ze_waaardo + "это..." + "\n\nЧтобы дать ответ просто напишите его в чат.")


@dp.message_handler(lambda message: message.text == "Сложные вопросы по теме \"Человек и общество\"")
async def button_hard_quest(message: types.Message):
    global hard
    global hard_words_next
    global hard_words
    global mode
    mode = 2
    hard = random.choice(harder)
    hard_words = hard.split(":")
    naruto = hard_words[1]
    hard_words_next = naruto.strip()
    jojo = hard_words[0]
    print("Назовите " + str(jojo))
    print(hard)
    await bot.send_message(message.chat.id, text = "Назовите " + str(jojo) + ":" + "\n\nЧтобы дать ответ просто напишите его в чат.")



@dp.message_handler(lambda message: message.text == "Посмотреть правильный ответ ✅")
async def give(message: types.Message):
    await bot.send_message(message.chat.id, text = str(defin), reply_markup=kb.makup_begin)


@dp.message_handler(lambda message: message.text == "Посмотреть правильный ответ✅")
async def hard_give(message: types.Message):
    await bot.send_message(message.chat.id, text = str(hard.capitalize()), reply_markup=kb.makup_begin)
# keyboards reply


@dp.message_handler(lambda message: message.text == "Экономика")
async def economic(message: types.Message):
    await bot.send_message(message.chat.id, text = "Вопросы будут пополняться со временем.", reply_markup=kb.makup_choice_econom)


@dp.message_handler(lambda message: message.text == "Определения по теме \"Экономика\"")
async def deffins_econom(message: types.Message):
    global economic # то про чо надо спросить
    global econom
    global true_econom # ответ
    global mode
    mode = 3
    econom = random.choice(deffi)
    econom_next = econom.split("-")
    true_econom = econom_next[1]
    economic = econom_next[0].lstrip()
    print(economic + "это...")
    print(econom)
    await bot.send_message(message.chat.id, text = str(economic) + "это...\n\nЧтобы дать ответ просто напишите его в чат.")

@dp.message_handler(lambda message: message.text == "Сложные вопросы по теме \"Экономика\"")
async def harder_econom(message: types.Message):
    global hard_econom
    global true_hard
    global hardec
    global mode
    mode = 4
    hardec = random.choice(hards)
    hard_eco_next = hardec.split(":")
    true_hard = hard_eco_next[1]
    hard_econom = hard_eco_next[0].lstrip()
    print(hard_econom)
    print(hardec.capitalize())
    await bot.send_message(message.chat.id, text = "Назовите " + str(hard_econom) + ":" + "\n\nЧтобы дать ответ просто напишите его в чат.")


@dp.message_handler(lambda message: message.text == "Посмотреть ответ✅")
async def give(message: types.Message):
    await bot.send_message(message.chat.id, text = str(econom), reply_markup=kb.makup_choice_econom)


@dp.message_handler(lambda message: message.text == "Посмотреть ответ ✅")
async def hard_give(message: types.Message):
    await bot.send_message(message.chat.id, text = str(hardec.capitalize()), reply_markup=kb.makup_choice_econom)









@dp.message_handler(lambda message: message.text == "Политика")
async def politic(message: types.Message):
    await bot.send_message(message.chat.id, text = "Вы такое ещё не проходили.", reply_markup=kb.makup_block)


@dp.message_handler(lambda message: message.text == "Право")
async def pravo(message: types.Message):
    await bot.send_message(message.chat.id, text = "Вы такое ещё не проходили.", reply_markup=kb.makup_block)





@dp.message_handler(lambda message: message.text.lower())
async def suka(message: types.Message):
    r = message.text
    if mode == 1:
        a = fuzz.token_sort_ratio(r, word_next)
        await message.reply("Ваше определение схоже с моим на " + str(a) + " %", reply_markup=kb.makup_return)
        # if a <= 90:
        #     user_id = message.from_user.id
        #     k = open(str(user_id)+".txt", "a+", encoding="utf-8")
    elif mode == 2:
        a = fuzz.token_sort_ratio(r, hard_words_next)
        await message.reply("Ваше определение схоже с моим на " + str(a) + " %", reply_markup=kb.makup_hard_return)
        # if a <= 90:
        #     user_id = message.from_user.id
        #     k = open(str(user_id)+".txt", "a+", encoding="utf-8")
    elif mode == 3:
        a = fuzz.token_sort_ratio(r, true_econom)
        await message.reply("Ваше определение схоже с моим на " + str(a) + " %", reply_markup=kb.makup_returns)
        # if a <= 90:
        #     user_id = message.from_user.id
        #     k = open(str(user_id)+".txt", "a+", encoding="utf-8")
    elif mode == 4:
        a = fuzz.token_sort_ratio(r, true_hard)
        await message.reply("Ваше определение схоже с моим на " + str(a) + " %", reply_markup=kb.makup_returns_hard)
        # if a <= 90:
        #     user_id = message.from_user.id
        #     k = open(str(user_id)+".txt", "a+", encoding="utf-8")








executor.start_polling(dp, skip_updates=True)



# озвучить зарондомленное определение
# @dp.message_handler(commands = "audio")
# async def audio(message: types.Message):
#     global word
#     global word_next
#     global defin
#     defin = random.choice(definitions)
#     word = defin.split("-")
#     sasuke = word[1]
#     word_next = sasuke.strip()
#     ze_waaardo = word[0]
#     print(str(ze_waaardo) + "это...")
#     print(str(defin))
#     tts = gTTS(str(ze_waaardo) + "это...", lang = "ru")
#     tts.save("audio.mp3")
#     f = open("audio.mp3", "rb")
#     await bot.send_voice(message.chat.id, f)