import logging
import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import os
GEMINI_API_KEY = AIzaSyAjNKWGMWVqMQ-a59tKLoe3ppX58RGUC0g
TOKEN = os.getenv("TOKEN")  8170787826:AAEdbyq9XZhSWSROoR4Zs0MVjFwhfw88YKg

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

support_responses = [
    "Я здесь, чтобы выговориться. Что у тебя на душе?",
    "Ты не один, я рядом. Расскажи, что случилось?",
    "Иногда просто нужно поговорить. Я слушаю!",
    "Ты сильный(ая), даже если сейчас кажется иначе.",
    "Помни, что после дождя всегда бывает солнце."
]

@dp.message_handler(commands=["start"])
async def send_welcome(message: Message):
    await message.reply("Привет! Я бот-психолог. Расскажи, что беспокоит, я постараюсь поддержать тебя.")

@dp.message_handler()
async def support_user(message: Message):
    response = random.choice(support_responses)
    await message.reply(response)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling())
    loop.run_forever()
