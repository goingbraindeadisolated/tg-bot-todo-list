"""Работа с базой данных"""
import sqlite3
import os
import re
connection = sqlite3.connect(os.path.join('db', 'tasks.db'))
cursor = connection.cursor()


def init_db():
	"""Создает таблицу с тасками для пользователя, если она не была создана до этого"""
	cursor.execute("CREATE TABLE IF NOT EXISTS tasks(chat_id INT, task TEXT)")
	connection.commit()

def add_task(chat_id:int, raw_msg:str):
	"""Добавляет задачу в базу данных"""
	task_text = _parse_message(raw_msg)
	cursor.executemany("INSERT INTO tasks(chat_id, task) VALUES(?, ?)", [(chat_id, task_text)])
	connection.commit()

def remove_task(chat_id:int, raw_msg:str):
	"""Удаляет задачу из базы данных"""
	task_id = int(_parse_message(raw_msg))
	task_text = get_list(chat_id)[task_id-1]
	cursor.executemany("DELETE FROM tasks WHERE chat_id=? AND task=?", [(chat_id, task_text)])
	connection.commit()

def get_list(chat_id:int)->list:
	"""Выводит список задач"""
	cursor.execute("SELECT task FROM tasks WHERE chat_id={}".format(chat_id))
	response = cursor.fetchall()
	return [task[0] for task in response]

def _parse_message(raw_msg:str)->str:
	return re.split(r'/\w* ', raw_msg)[1]

init_db()
