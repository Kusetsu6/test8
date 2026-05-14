import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

API_TOKEN = "8756157675:AAHO6Nk1hJUtNvs_y3-LF9EgFjhjmlnSK34"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Створюємо шаблон callback_data
buy_callback = CallbackData("buy", "item")

# /shop команда
@dp.message(Command("shop"))
async def show_shop(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🍎 Яблуко", callback_data=buy_callback.new(item="apple"))],
            [InlineKeyboardButton(text="🍌 Банан", callback_data=buy_callback.new(item="banana"))],
            [InlineKeyboardButton(text="🍇 Виноград", callback_data=buy_callback.new(item="grape"))],
        ]
    )
    await message.answer("Що хочеш купити?", reply_markup=keyboard)

# Обробка callback_data за шаблоном
@dp.callback_query(buy_callback.filter())
async def handle_buy_callback(callback: CallbackQuery, callback_data: dict):
    item = callback_data["item"]
    await callback.message.answer(f"Ти обрав: {item.capitalize()} ✅")
    await callback.answer()

# Запуск
async def main():
    print("Бот запущений...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
