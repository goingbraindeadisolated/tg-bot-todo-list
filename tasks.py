import re
import datetime
import db
from typing import NamedTuple
from aiogram.utils.markdown import bold, code, italic, text
from aiogram.utils.emoji import emojize


numbers = {
    1: ':one:',
    2: ':two:',
    3: ':three:',
    4: ':four:',
    5: ':five:',
}


class Task(NamedTuple):
    title: str
    text:str
    timestamp:str
    #marks:list

def _parse_msg(raw_msg:str)->str:
    """
    Из сообщения с командной получает только сообщение
    Изначально сообщение выглдяит как '/command message'
    Из него нужно получить message
    return:message
    """
    msg = re.split('/\w* ', raw_msg)[1]
    return msg

def _parse_task(msg:str)->Task:
    """
    Сообщение выглядит как '<task_title> task_text'
    Из него нужно получить title и text
    """
    if re.search('\<\S*\>', msg) is not None:
        title = re.search('\<\S*\>', msg)[0][1:-1]
        text = re.split(title, msg)[1][1:]
    else:
        title = ''
        text = msg
    return (title, text)

def add_task(chat_id:int, raw_msg:str):
    msg = _parse_msg(raw_msg)
    title, text = _parse_task(msg)
    db.insert('tasks_t', {
        'chat_id': str(chat_id),
        'task_title': title,
        'task_text': text
        })

def remove_task(chat_id:int, raw_msg:str)->bool:
    task_id = int(_parse_msg(raw_msg)) 
    task_list = _get_task_list(chat_id)
    task = task_list[task_id-1]
    db.delete('tasks_t',{
        'chat_id': chat_id,
        'task_text': task.text,
        'task_title': task.title
        })

def _get_task_list(chat_id:int)->list:
    db_list = db.select('tasks_t', chat_id)
    tasks = [Task(title, text, timestamp) for _, title, text, timestamp in db_list]
    return tasks

def get_tasks(chat_id:int)->list:
    task_list = _get_task_list(chat_id)
    tasks = []
    for i, task in enumerate(task_list):
        formatted_task = f"({i+1}) {task.title}\n \
        <i>{task.text}</i>\n"
        tasks.append(formatted_task)
    return tasks 
