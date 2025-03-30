import os
import logging
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Настройки
TOKEN = "8170787826:AAEdbyq9XZhSWSROoR4Zs0MVjFwhfw88YKg"
GEMINI_API_KEY = "AIzaSyAjNKWGMWVqMQ-a59tKLoe3ppX58RGUC0g"

# Логирование
logging.basicConfig(level=logging.INFO)

# Настройка API Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Создание бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Обработчик сообщений
@dp.message_handler()
async def chat_with_ai(message: types.Message):
    try:
        response = model.generate_content(message.text)
        await message.answer(response.text)
    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await message.answer("Произошла ошибка при обработке запроса.")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
