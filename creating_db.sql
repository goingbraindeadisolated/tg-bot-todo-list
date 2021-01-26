BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS'tasks_t'(
    'chat_id' INTEGER,
    'task_title' TEXT,
    'task_text' TEXT,
    'timestamp' timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, 
    'current_state' INTEGER
);
CREATE TABLE IF NOT EXISTS 'users_t'(
    'chat_id' INTEGER,
    'state' INTEGER
);
COMMIT;