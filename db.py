"""Работа с базой данных"""
import sqlite3
import os
import re
connection = sqlite3.connect(os.path.join('db', 'tasks.db'))
cursor = connection.cursor()


def init_db():
	"""Создает таблицу с тасками для пользователя, если она не была создана до этого"""
	cursor.execute("CREATE TABLE IF NOT EXISTS tasks(chat_id INT, task_title TEXT, task_text TEXT)")
	connection.commit()

def insert(columns:dict):
	"""
	columns: Словарь с названием колонок и их значениями,
	 которые нужно добавить в таблицу
	"""
	pass

def delete(columns:dict)->bool:
	"""
	columns: Словарь с названием колонок и их значениями.
	 По этим данным происходит удаление строк из таблицы
	return: Если что-то удалилось, то True. Если нет, False. 
	"""
	pass

def select(columns:dict)->List[Tuple]:
	"""
	columns: Словарь с названием колонок и их значениями.
	 По этим данным ищутся строки из таблицы.
	 
	"""
	pass

init_db()
