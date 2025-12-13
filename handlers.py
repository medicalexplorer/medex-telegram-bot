from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import (
    main_menu_kb,
    back_kb,
    BTN_TESTS,
    BTN_TASKS,
    BTN_STATS,
    BTN_LEADERBOARD,
    BTN_CABINET,
    BTN_COMMUNITY,
    BTN_INFO,
    BTN_BACK,
)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать в MEDEX.\n\nВыберите раздел:",
        reply_markup=main_menu_kb(),
    )


@router.message(F.text == BTN_TESTS)
async def on_tests(message: Message):
    await message.answer("Тесты — раздел в работе.", reply_markup=back_kb())


@router.message(F.text == BTN_TASKS)
async def on_tasks(message: Message):
    await message.answer("Задания — раздел в работе.", reply_markup=back_kb())


@router.message(F.text == BTN_STATS)
async def on_stats(message: Message):
    await message.answer("Статистика — раздел в работе.", reply_markup=back_kb())


@router.message(F.text == BTN_LEADERBOARD)
async def on_leaderboard(message: Message):
    await message.answer("Лидерборд — раздел в работе.", reply_markup=back_kb())


@router.message(F.text == BTN_CABINET)
async def on_cabinet(message: Message):
    await message.answer("Личный кабинет — раздел в работе.", reply_markup=back_kb())


@router.message(F.text == BTN_COMMUNITY)
async def on_community(message: Message):
    await message.answer("Сообщество — раздел в работе.", reply_markup=back_kb())


