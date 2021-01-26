from enum import Enum
import db

class States(Enum):
    S_IDLE = 0
    S_TASK_EDITING = 1 
    S_TASK_INPUT = 2

def get_current_state(chat_id:int)->int:
    return db.select('users_t', chat_id)[1]

def set_state(chat_id, state:int):
    db.update(
        'users_t',
        {'state':state},
        {'chat_id': chat_id}
        )