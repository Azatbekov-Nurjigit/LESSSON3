
from aiogram import Bot , Dispatcher
from decouple import config
TOKEN = config("TOKEN")
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
dp = Dispatcher(bot=bot, storage=storage)




TOKEN = config("TOKEN")

