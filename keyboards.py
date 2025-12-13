from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

BTN_TESTS = "🧪 Тесты"
BTN_TASKS = "🎯 Задания"
BTN_STATS = "📊 Статистика"
BTN_LEADERBOARD = "🏆 Лидерборд"
BTN_CABINET = "👤 Личный кабинет"
BTN_COMMUNITY = "🌍 Сообщество"
BTN_INFO = "ℹ️ Информация"
BTN_BACK = "⬅️ Назад"


def main_menu_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=BTN_TESTS), KeyboardButton(text=BTN_TASKS)],
            [KeyboardButton(text=BTN_STATS), KeyboardButton(text=BTN_LEADERBOARD)],
            [KeyboardButton(text=BTN_CABINET), KeyboardButton(text=BTN_COMMUNITY)],
            [KeyboardButton(text=BTN_INFO)],
        ],
        resize_keyboard=True,
    )


def back_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=BTN_BACK)]],
        resize_keyboard=True,
    )
