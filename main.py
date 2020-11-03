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
  pass

@dp.message_handler(commands=['addt'])
async def add_task(message: types.Message):
	pass

@dp.message_handler(commands=['t'])
async def task(message: types.Message):
	pass

@dp.message_handler(commands=['rmt'])
async def remove_task(message: types.Message):
	pass

@dp.message_handler(commands=['tasks'])
async def get_tasks(message: types.Message):
	pass

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)


