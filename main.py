#news by preferens bot
import asyncio
import datetime
import json
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hlink
from aiogram.dispatcher.filters import Text
from config import token, user_id
from scraping2 import get_first_news2
from scraping1 import get_first_news
import keyboards as kb

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
connect = sqlite3.connect('users.db')
cursor = connect.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users(id      INTEGER PRIMARY KEY,'
                   ' user_id INT     UNIQUE,'
                   ' name    TEXT    NOT NULL)')
@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("""Привет!
    Этот бот поможет тебе быть в курсе событей одним из первых
    """, reply_markup=kb.inline_kb_full)

    cursor.execute("""INSERT INTO users (user_id, name) VALUES(?, ?)""", [message.chat.id, message.chat.first_name])
    cursor.close()
    connect.commit()
    #connect.close()

@dp.callback_query_handler(text='btn2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Новости спорта', reply_markup=kb.markup3)
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)

@dp.message_handler(Text(equals="Последниe 5 новостей"))
async def get_last_five_news(message: types.Message):
    with open("news_dict1.json", encoding='utf-8') as file:
        news1_dict = json.load(file)

    for k, v in sorted(news1_dict.items())[-5:]:
        news = f"{hlink(v['article_title'], v['article_url'])}"

        await message.answer(news)



@dp.callback_query_handler(text='btn1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Новости технологий', reply_markup=kb.markup4)
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)



@dp.message_handler(Text(equals="Последниe 5 новостeй"))
async def get_last_five_news(message: types.Message):

    with open("news_dict.json", encoding='utf-8') as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items())[:5]:
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
               f"{hlink(v['article_title'], v['article_url'])}"

        await message.answer(news)






@dp.message_handler(Text(equals='Меню'))
async def news(mesg: types.Message):
    text_answer = ('Выберите тему и будьте в курсе каждцй день')
    await mesg.answer(text_answer, reply_markup=types.ReplyKeyboardRemove())
    await mesg.answer('Темы', reply_markup=kb.inline_kb_full)




if __name__ == '__main__':
    get_first_news()
    get_first_news2()
    executor.start_polling(dp, skip_updates=True)
