import logging 
import dotenv
import os
import tasks
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.emoji import emojize
from aiogram.utils.markdown import bold, code, italic, text
from aiogram.types import ParseMode
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

dotenv.load_dotenv()
bot = Bot(token=os.getenv('API_KEY'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup([
		[emojize(':heavy_plus_sign:Добавить задачу')],
		[emojize(':heavy_minus_sign:Удалить задачу')],
		[emojize(':clipboard:Список задач')],
		[emojize(':page_facing_up:Редактировать задачу')]
		], resize_keyboard=True)
	await message.answer(emojize('''
:wave:*Привет*, я - бот, который поможет тебе с менеджментом твоих задач

*Что я могу*:
:frame_with_picture:Прикреплять медиа-файлы к задачам
:pencil2:Записывать и удалять задачи
:memo:Редактировать задачи
:bell:Напоминать о задачах

Если есть какие-то пожелания, пишите сюда @renuuut
	'''),
	 parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard)

@dp.message_handler(commands=[emojize(':heavy_plus_sign:Добавить задачу')])
async def add_task(message: types.Message):
	await message.answer('Введите текст задачи')	
	tasks.add_task(message.chat.id, message.text)
	await message.answer('Задача успешно добавлена') 

#test
@dp.message_handler()
async def test(message: types.Message):
	inline_kb1 = InlineKeyboardMarkup(row_width=5)
	numbers_emjs = [':one:', ':two:', ':three:', ':four:', ':five:']
	arrows_emjs = [':arrow_forward:']
	msg1 =f'''
Ваши текущие задачи

_страница 1 из 1_

{numbers_emjs[0]}*Заголовок тестовой задачи номер 1*
_Текст тестовой задачи номер 1_
{numbers_emjs[1]}*Заголовок тестовой задачи номер 2*
_Текст тестовой задачи номер 2_
{numbers_emjs[2]}*Заголовок тестовой задачи номер 3*
_Текст тестовой задачи номер 3_
{numbers_emjs[3]}*Заголовок тестовой задачи номер 4*
_Текст тестовой задачи номер 4_
{numbers_emjs[4]}*Заголовок тестовой задачи номер 5*
_Текст тестовой задачи номер 5_
'''
	msg2 = 'Введите текст задачи'
	msg3 = 'Задача номер 2 успешно удалена'
	msg4 = 'Введите номер задачи, которую нужно удалить'
	msg5 =f''' 
Ваши текущие задачи

_страница 1 из 1_

{numbers_emjs[0]}*Заголовок тестовой задачи номер 1*
_Текст тестовой задачи номер 1_
{numbers_emjs[1]}*Заголовок тестовой задачи номер 3*
_Текст тестовой задачи номер 3_
{numbers_emjs[2]}*Заголовок тестовой задачи номер 4*
_Текст тестовой задачи номер 4_
{numbers_emjs[3]}*Заголовок тестовой задачи номер 5*
_Текст тестовой задачи номер 5_
'''
	numbers = [inline_kb1.insert(InlineKeyboardButton(text=emojize(number_emj), callback_data='data')) for number_emj in numbers_emjs]
	arrows = [inline_kb1.insert(InlineKeyboardButton(text=emojize(arrow_emj), callback_data='data')) for arrow_emj in arrows_emjs]
	await message.answer(emojize(msg5), parse_mode=ParseMode.MARKDOWN, reply_markup=inline_kb1)	

@dp.message_handler(commands=['t'])
async def task(message: types.Message):
	pass

@dp.message_handler(commands=['rmt'])
async def remove_task(message: types.Message):
	tasks.remove_task(message.chat.id, message.text)
	await message.answer('Задача успешно удалена') 

@dp.message_handler(commands=['tasks'])
async def get_tasks(message: types.Message):
	msg = ''.join(tasks.get_tasks(message.chat.id))
	msg = '<b>Список задач</b>\n\n' + msg
	await message.answer(msg, parse_mode='HTML')

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)

