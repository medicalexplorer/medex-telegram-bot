from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(commands=["start"])
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать в MEDEX!\n"
        "Для продолжения подпишитесь на наши каналы:\n\n"
        "• https://t.me/medicalexplorer\n"
        "• https://t.me/medexannouncements\n\n"
        "После подписки нажмите кнопку /start снова."
    )
