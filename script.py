from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from funcs import get_page
#from states import MyStates
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


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
    language_button_ru = InlineKeyboardButton('Русский', callback_data='ru')
    language_button_en = InlineKeyboardButton('Английский', callback_data='en')
    set_language_keyboard = InlineKeyboardMarkup().add(
        language_button_ru, language_button_en)
    if message.text == 'Получить рандомную статью':

        await message.reply('Какой язык должен быть у статьи?', reply_markup=set_language_keyboard)


@dp.callback_query_handler(lambda c: c.data == 'ru')
async def process_callback_for_rulang(callback_query: types.CallbackQuery):
    #await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, get_page('ru'))


@dp.callback_query_handler(lambda c: c.data == 'en')
async def process_callback_for_enlang(callback_query: types.CallbackQuery):
    #await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, get_page('en'))


if __name__ == "__main__":
    executor.start_polling(dp)
