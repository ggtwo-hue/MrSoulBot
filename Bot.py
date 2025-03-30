import os
import logging
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Твой API-ключ Gemini
GEMINI_API_KEY = "AIzaSyAjNKWGMWVqMQ-a59tKLoe3ppX58RGUC0g"

# Твой Telegram Bot Token
TOKEN = "8170787826:AAEdbyq9XZhSWSROoR4Zs0MVjFwhfw88YKg"

# Настройка Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Настройка бота
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Функция для общения с Gemini
def ask_gemini(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return "Ошибка при обработке запроса. Попробуйте позже."

# Обработчик сообщений
@dp.message_handler()
async def chat_with_gemini(message: types.Message):
    user_question = message.text
    bot_response = ask_gemini(user_question)
    await message.reply(bot_response)

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
