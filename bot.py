import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

API_TOKEN = "8756157675:AAHO6Nk1hJUtNvs_y3-LF9EgFjhjmlnSK34"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привіт, я твій бот! Напиши /help, щоб дізнатися, що я вмію.")

# /help
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Команди:\n/start — запуск\n/help — допомога\n/joke — жарт\n/about - про мене\n/bye — прощання")

# /joke
@dp.message(Command("joke"))
async def joke_command(message: Message):
    await message.answer("Колобок повісивси!")

# /about
@dp.message(Command("about"))
async def about_command(message: Message):
    await message.answer("цей бот створив Володька")

@dp.message(Command("quize"))
async def quize_command(message: Message):
    await message.answer("Найпершим аніме в історії вважається короткометражний фільм «Namakura Gatana» («Тупий меч»), випущений у 1917 році. Це німа чорно-біла робота тривалістю близько 2 хвилин, створена режисером Дзюнічі Коучі. У ньому розповідається комічна історія про самурая, який купив тупий меч.")


# /bye
@dp.message(Command("bye"))
async def bye_command(message: Message):
    await message.answer("До побачення! Гарного дня 😊")

# Обробка звичайного тексту
@dp.message()
async def echo_text(message: Message):
    text = message.text.lower()
    if "привіт" in text:
        await message.answer("Привіт! Гарного настрою 😄")
    elif "як справи" in text:
        await message.answer("У мене все супер, дякую! А в тебе?")
    else:
        await message.answer("їде п'яний чоловік в трамваї і говорить: "
                             "- зара дорахую до 48 і почну ригати "
                             "пасажири подумали, що поки дощитає встигнуть вийти "
                             "Пяниця: 6*8=48"
                             )



# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
