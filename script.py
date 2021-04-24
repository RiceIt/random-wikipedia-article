from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from funcs import get_page
#from PGDB import db, cursor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
#from states import MyStates


token = '1728839487:AAEmQMeRNhJXWyAoGs9sr8w1IL3yDbEnQkA'

# Initialize bot and dispatcher
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


button_hi = KeyboardButton('Получить рандомную статью')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(button_hi)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply('Привет, нажми кнопку', reply_markup=greet_kb)


@dp.message_handler(content_types=['text'])
async def main(message):

    if message.text == 'Получить рандомную статью':

        await bot.send_message(message.chat.id, get_page())


if __name__ == "__main__":
    executor.start_polling(dp)
