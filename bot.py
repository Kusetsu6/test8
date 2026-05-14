import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = "8756157675:AAHO6Nk1hJUtNvs_y3-LF9EgFjhjmlnSK34"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Команда /menu показує кнопки
@dp.message(Command("menu"))
async def show_menu(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Привіт 👋"), KeyboardButton(text="Як справи? 😊")],
            [KeyboardButton(text="Анекдот 🤣")]
        ],
        resize_keyboard=True
    )
    await message.answer("Вибери опцію:", reply_markup=keyboard)

# Обробка натискань
@dp.message()
async def handle_message(message: Message):
    text = message.text
    if text == "Привіт 👋":
        await message.answer("Привіт-привіт! 👋")
    elif text == "Як справи? 😊":
        await message.answer("Усе чудово! А в тебе?")
    elif text == "Анекдот 🤣":
        await message.answer("Як називається кіт-програміст? — JavaMeow!")
    else:
        await message.answer("Натисни одну з кнопок 😺")

async def main():
    print("Бот запущений...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
