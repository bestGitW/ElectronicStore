import sqlite3
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from db_api import Database


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db_path = Path('db_api', 'database', 'shop_database.db')
db = Database(db_path=db_path)
try:
    db.create_table_users()
except sqlite3.OperationalError as e:
    print(e)
except Exception as e:
    print(e)

try:
    db.create_table_items()
except sqlite3.OperationalError as e:
    print(e)
except Exception as e:
    print(e)

try:
    db.create_table_basket()
except sqlite3.OperationalError as e:
    print(e)
except Exception as e:
    print(e)