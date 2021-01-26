"""Работа с базой данных"""
import sqlite3
import os
from typing import NamedTuple

connection = sqlite3.connect(os.path.join('db', 'tasks_db.db'))
cursor = connection.cursor()

#TODO: как хранить задачи и состояния вмсете?
#Создать другую таблицу аалхаха
def init_db():
	with open('creating_db.sql') as db:
		db = db.read()
		cursor.executescript(db)
		connection.commit()

def insert(table:str, payload:dict):
	#TODO: Сюда бы трай эксцепт добавить на случай ввода неверных названий колонок
	placeholders = ", ".join( "?" * len(payload.keys()) )
	columns = ', '.join(payload.keys())
	values = tuple(payload.values())
	cursor.execute(f"INSERT INTO {table} ({columns}) VALUES ({placeholders})", values)
	connection.commit()

def delete(table:str, payload:dict)->bool:
	column_value = ' AND '.join([f'{column}={value}' for column, value in payload.items()])
	response = cursor.execute(
		f"DELETE FROM {table} WHERE {colunm_value}")
	print(response)
	connection.commit()

def select(table:str, chat_id:int)->list:
	cursor.execute(f"SELECT * FROM {table} WHERE chat_id={chat_id}")
	return cursor.fetchall()

def update(table:str, payload:dict, condition:dict):
	"""
	payload:словарь формата {столбец: значение} со значениями,
	 на которые нужно изменить
	condition: словарь формата {столбец: значение},
	 необходимый для поиска строки в которой будут изменяться значения 
	"""
	column_value = ','.join([f'{column}={value}' for column, value in payload.items()])
	condition = 'AND '.join([f'{column}={value}' for column, value in condition.items()])
	cursor.execute(f"UPDATE {table} SET {column_value} WHERE {condition}")
	
init_db()
