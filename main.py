import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import BOT_TOKEN, WEBHOOK_URL

async def main():
    dp = Dispatcher()
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
