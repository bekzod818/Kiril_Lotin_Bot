import logging
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from transliterate import to_cyrillic, to_latin


API_TOKEN = TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def boshlash(message: types.Message):
    """Botga /start buyrug'i yozilganda ishga tushadi"""
    user = message.from_user.first_name
    await message.reply(f"Salom {user}")

@dp.message_handler()
async def echo(message: types.Message):
    msg = message.text
    if msg.isascii():
        cyril = to_cyrillic(msg)
        await message.answer(cyril)
    else:
        latin = to_latin(msg)
        await message.answer(latin)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)