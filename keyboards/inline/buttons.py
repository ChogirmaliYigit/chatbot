from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import bot


inline_keyboard = [[
    InlineKeyboardButton(text="✅ Yes", callback_data='yes'),
    InlineKeyboardButton(text="❌ No", callback_data='no')
]]
are_you_sure_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


async def subscribe_markup(chat_ids: list[int]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"{chat.title}", url=chat.invite_link or f"https://t.me/{chat.username}"),
            ] for chat in [await bot.get_chat(chat_id=_id) for _id in chat_ids]
        ],
    )
