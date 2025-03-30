import os
import logging
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Твой API-ключ Gemini
GEMINI_API_KEY = "AIzaSyAjNKWGMWVqMQ-a59tKLoe3ppX58RGUC0g"

# Твой Telegram Bot Token
TOKEN = "8170787826:AAEdbyq9XZhSWSROoR4Zs0MVjFwhfw88YKg"

# Настройка Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Настройка бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Функция для общения с Gemini
def ask_gemini(question):
    try:
        logging.info(f"Отправляем вопрос в Gemini: {question}")
        response = model.generate_content(question)
        logging.info(f"Ответ от Gemini: {response.text}")
        return response.text
    except Exception as e:
        logging.error(f"Ошибка при запросе к Gemini: {e}")
        return f"Ошибка: {str(e)}"

# Обработчик сообщений
@dp.message_handler()
async def chat_with_gemini(message: types.Message):
    user_question = message.text
    bot_response = ask_gemini(user_question)
    await message.reply(bot_response)

# Запуск бота
if __name__ == "__main__":
    logging.info("Бот запущен!")
    executor.start_polling(dp, skip_updates=True)
