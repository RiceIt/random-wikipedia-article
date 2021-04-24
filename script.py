import os

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from funcs import get_page
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


token = os.environ["TOKEN"]

# Initialize bot and dispatcher
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    rangom_article_button = KeyboardButton('Получить рандомную статью')

    random_article_keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True).add(rangom_article_button)
    await message.reply('Привет, нажми кнопку', reply_markup=random_article_keyboard)


@dp.message_handler(content_types=['text'])
async def main(message):
    language_button_ru = KeyboardButton('Статья на русском')
    language_button_en = KeyboardButton('Статья на английском')
    set_language_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
        language_button_ru, language_button_en)

    if message.text == 'Получить рандомную статью':
        await message.reply('Какой язык должен быть у статьи?', reply_markup=set_language_keyboard)

    elif message.text == 'Статья на русском':
        await bot.send_message(message.chat.id, get_page('ru'))
    elif message.text == 'Статья на английском':
        await bot.send_message(message.chat.id, get_page('en'))


if __name__ == '__main__':
    executor.start_polling(dp)
