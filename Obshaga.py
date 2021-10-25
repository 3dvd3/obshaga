import logging
import random
from aiogram.types import message

import keyboards as kb

from aiogram import Bot, types # импорт типов
from aiogram.dispatcher import Dispatcher # это просто надо смирись 
from aiogram.utils import executor

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from Config import BOT_TOKEN
from definitions import definitions
from definitions import harder
from gtts import gTTS


bot = Bot(token = BOT_TOKEN)

dp = Dispatcher(bot)

logging.basicConfig(level=logging.ERROR)



# default commands
@dp.message_handler(commands = "start")
async def start(message: types.Message):
    await bot.send_message(message.chat.id, text = "Привет, я бот для подготовки к ЕГЭ по обществознанию!\n\nДля начала выберите блок задании", reply_markup=kb.makup_theme)
    file = r"C:\Users\Totosa\Desktop\obshaga\NameID.txt"
    k = message.from_user.id
    name = message.from_user.username
    c = open(file, "a+", encoding='utf-8')
    c.write("Username: " + str(name) + ";" + " ID: " + str(k) + "\n")
    c.close
    uniqlines = set(open(file,'r', encoding='utf-8').readlines())
    gotovo = open(file,'w', encoding='utf-8').writelines(set(uniqlines))




@dp.message_handler(commands = "users")
async def info(message: types.Message):
    k = open("NameID.txt", "r", encoding="UTF-8")
    contents = k.readlines()
    print(contents)
    c = "".join(contents)
    await message.reply("Все, кто писал боту:\n" + str(c))
# default commands


# reply - question commands
@dp.message_handler(commands = "d")
async def defin(message: types.Message):
    global word
    global word_next
    global defin
    defin = random.choice(definitions)
    word = defin.split("-")
    sasuke = word[1]
    word_next = sasuke.strip()
    ze_waaardo = word[0]
    print(str(ze_waaardo) + "это...")
    print(str(defin))
    await bot.send_message(message.chat.id, text = ze_waaardo + "это..." + "\n\nЧтобы дать ответ напишите /a *ответ*.")

@dp.message_handler(commands = "a")
async def answer(message: types.Message):
    ans = message.text.split("/a")
    answer = ans[1]
    print(answer.strip())
    a = fuzz.token_sort_ratio(answer, word_next)
    await message.reply("Ваше определение схоже с моим на " + str(a) + " %", reply_markup=kb.makup_return)

@dp.message_handler(commands = "p")
async def hard(message: types.Message):
    global hard
    global hard_words_next
    global hard_words
    hard = random.choice(harder)
    hard_words = hard.split(":")
    naruto = hard_words[1]
    hard_words_next = naruto.strip()
    jojo = hard_words[0]
    print("Назовите " + str(jojo))
    print(hard)
    await bot.send_message(message.chat.id, text = "Назовите " + str(jojo) + ":" + "\n\nЧтобы дать ответ напишите /ap *ответ*.")

@dp.message_handler(commands = "ap")
async def hard_answer(message: types.Message):
    ans = message.text.split("/ap")
    answer = ans[1]
    print(answer.strip())
    a = fuzz.token_sort_ratio(answer, hard_words_next)
    await message.reply("Ваше определение схоже с моим на " + str(a) + " %", reply_markup=kb.makup_hard_return)
# reply - question commands



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
    defin = random.choice(definitions)
    word = defin.split("-")
    sasuke = word[1]
    word_next = sasuke.strip()
    ze_waaardo = word[0]
    print(str(ze_waaardo) + "это...")
    print(str(defin))
    await bot.send_message(message.chat.id, text = ze_waaardo + "это..." + "\n\nЧтобы дать ответ напишите /a *ответ*.")


@dp.message_handler(lambda message: message.text == "Сложные вопросы по теме \"Человек и общество\"")
async def button_hard_quest(message: types.Message):
    global hard
    global hard_words_next
    global hard_words
    hard = random.choice(harder)
    hard_words = hard.split(":")
    naruto = hard_words[1]
    hard_words_next = naruto.strip()
    jojo = hard_words[0]
    print("Назовите " + str(jojo))
    print(hard)
    await bot.send_message(message.chat.id, text = "Назовите " + str(jojo) + ":" + "\n\nЧтобы дать ответ напишите /ap *ответ*.")



@dp.message_handler(lambda message: message.text == "Посмотреть правильный ответ ✅")
async def give(message: types.Message):
    await bot.send_message(message.chat.id, text = str(defin), reply_markup=kb.makup_begin)


@dp.message_handler(lambda message: message.text == "Посмотреть правильный ответ✅")
async def hard_give(message: types.Message):
    await bot.send_message(message.chat.id, text = str(hard.capitalize()), reply_markup=kb.makup_begin)
# keyboards reply 




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