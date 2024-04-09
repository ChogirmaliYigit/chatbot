from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message
from aiogram.enums.chat_member_status import ChatMemberStatus
from loader import bot
from data.config import CHANNEL_ID
from keyboards.inline.buttons import subscribe_markup


class MemberMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        chat_member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        if chat_member.status not in [ChatMemberStatus.CREATOR, ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR]:
            chat = await bot.get_chat(chat_id=CHANNEL_ID)
            await event.answer(
                f"Siz {chat.title} kanaliga obuna bo'lmagansiz. Fikr qoldirish uchun avval obuna bo'ling.",
                reply_markup=await subscribe_markup([int(CHANNEL_ID)]),
            )
            return
        else:
            return await handler(event, data)
