from aiogram import executor

from bot import on_startup
from loader import dp

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)