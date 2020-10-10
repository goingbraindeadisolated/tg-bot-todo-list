import logging 
import dotenv
import os
from aiogram import Bot, Dispatcher, executor, types

import db
logging.basicConfig(level=logging.INFO)

dotenv.load_dotenv()
bot = Bot(token=os.getenv('API_KEY'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
  await message.answer(
    "Бот менеджер задач\n\n"
    "• /t -> добавить задачу\n"
    "• /rt -> убрать задачу\n"
    "• /l -> список задач"
  )

@dp.message_handler(commands=['t'])
async def add_task(message: types.Message):
	db.add_task(message.chat.id, message.text)
	await get_list(message)

@dp.message_handler(commands=['rt'])
async def remove_task(message: types.Message):
	db.remove_task(message.chat.id, message.text)
	await get_list(message)

@dp.message_handler(commands=['l'])
async def get_list(message: types.Message):
	task_list = db.get_list(message.chat.id)
	if task_list:
		msg = [str(i+1)+'. '+task_list[i]+'\n' for i in range(len(task_list))]
		msg = ''.join(msg)
	else:
		msg = 'Нет активных задач'
	await message.answer(msg)

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)


