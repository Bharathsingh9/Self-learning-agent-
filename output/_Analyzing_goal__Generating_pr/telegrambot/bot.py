from aiogram import Bot, Dispatcher, executor, types
import json

bot = Bot(token='YOUR_BOT_TOKEN')
dispatcher = Dispatcher(bot)

def start():
    executor.start_polling(dispatcher, skip_updates=True)

if __name__ == '__main__':
    start()