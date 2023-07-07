#news by preferens botkeyboards

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

inline_kb_full = InlineKeyboardMarkup(row_width=3)
inline_btn_1 = InlineKeyboardButton('Новости технологий', callback_data='btn1')
inline_btn_2 = InlineKeyboardButton('Новости спорта', callback_data='btn2')


inline_kb_full.add(inline_btn_1, inline_btn_2)





reply_btn_ = KeyboardButton('Каталог новостей')

markup2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup2.row(reply_btn_)




reply_btn_1 = KeyboardButton('Последниe 5 новостей')
reply_btn_3 = KeyboardButton('Меню')
markup3 = ReplyKeyboardMarkup(resize_keyboard=True)
markup3.row(reply_btn_1)
markup3.row(reply_btn_3)

replys_btn_1 = KeyboardButton('Последниe 5 новостeй')
replys_btn_3 = KeyboardButton('Меню')
markup4 = ReplyKeyboardMarkup(resize_keyboard=True)
markup4.row(replys_btn_1)
markup4.row(reply_btn_3)

"""#SMM_service
@dp.callback_query_handler(text="btn1")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата 1 кнопка!')
#design_service
@dp.callback_query_handler(text="btn2")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата 2 кнопка!')
#Mobile application development
@dp.callback_query_handler(text="btn3")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата 3 кнопка!')
"""

"""@dp.message_handler(Text(equals="Каталог услуг"))
async def process_command_1(message: types.Message):
    await message.reply("Здесь представлены все наши услуги", reply_markup=kb.markup2)

@dp.message_handler(Text(equals="Назад"))
async def process_command_1(message: types.Message):
    await message.reply("Главное меню", reply_markup=kb.markup1)"""


"""
@dp.callback_query_handler(text='btnweb')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    #await bot.send_message(callback_query.from_user.id, 'ghbdtn')
    await callback_query.message.edit_text(text="тру")


    #await callback_query.message.edit_reply_markup(reply_markup=kb.inline_kb_RC)
#await bot.send_message(callback_query.from_user.id, 'Информация')

@dp.callback_query_handler(text='btnavto')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    #await bot.edit_message_text('qqqqqq')
    await callback_query.message.edit_text(text="тр")
"""