import logging
import random
from aiogram.types import message

from wikipedia.wikipedia import languages
import keyboards as kb

from aiogram import Bot, types # импорт типов
from aiogram.dispatcher import Dispatcher # это просто надо смирись 
from aiogram.utils import executor

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from Config import BOT_TOKEN
from definitions import definitions
from definitions import harder

bot = Bot(token = BOT_TOKEN)

dp = Dispatcher(bot)

logging.basicConfig(level=logging.ERROR)

@dp.message_handler(commands = "start")
async def start(message: types.Message):
    await bot.send_message(message.chat.id, text = "Привет, я бот для подготовки к ЕГЭ по обществознанию!\n\nПроверить свои знания можно командами /d и /p\nИли с помощью кнопок ниже.", reply_markup=kb.makup_begin)


@dp.message_handler(lambda message: message.text == "Определения")
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

@dp.message_handler(lambda message: message.text == "Сложные вопросы")
async def button_hard_quest(message: types.Message):
    global hard
    global hard_words_next
    global hard_words
    hard = random.choice(harder)
    hard_words = hard.split(":")
    naruto = hard_words[1]
    hard_words_next = naruto.strip()
    jojo = hard_words[0]
    print("Перечислите " + str(jojo))
    print(hard)
    await bot.send_message(message.chat.id, text = "Перечислите " + str(jojo) + ":" + "\n\nЧтобы дать ответ напишите /ap *ответ*.")




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
    print(answer)
    a = fuzz.token_sort_ratio(answer, word_next)
    await message.reply("Ваше определение схоже с моим на " + str(a) + " %", reply_markup=kb.makup_return)

@dp.message_handler(lambda message: message.text == "Посмотреть правильный ответ ✅")
async def give(message: types.Message):
    await bot.send_message(message.chat.id, text = str(defin), reply_markup=kb.makup_begin)


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
    print("Перечислите " + str(jojo))
    print(hard)
    await bot.send_message(message.chat.id, text = "Перечислите " + str(jojo) + ":" + "\n\nЧтобы дать ответ напишите /ap *ответ*.")

@dp.message_handler(commands = "ap")
async def hard_answer(message: types.Message):
    ans = message.text.split("/ap")
    answer = ans[1]
    print(answer)
    a = fuzz.token_sort_ratio(answer, hard_words_next)
    await message.reply("Ваше определение схоже с моим на " + str(a) + " %", reply_markup=kb.makup_hard_return)


@dp.message_handler(lambda message: message.text == "Посмотреть правильный ответ✅")
async def hard_give(message: types.Message):
    await bot.send_message(message.chat.id, text = str(hard.capitalize()), reply_markup=kb.makup_begin)


executor.start_polling(dp, skip_updates=True)
