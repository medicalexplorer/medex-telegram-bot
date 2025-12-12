from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать в MEDEX!\n\n"
        "Для продолжения подпишитесь на наши каналы:\n\n"
        "🔹 https://t.me/medicalexplorer\n"
        "🔹 https://t.me/medexannouncements\n\n"
        "После подписки нажмите команду /start снова."
    )
