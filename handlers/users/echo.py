from aiogram import Router, types
from loader import bot
from data.config import ADMINS

router = Router()


@router.message()
async def feedback(message: types.Message):
    for admin in ADMINS:
        try:
            await bot.forward_message(admin, message.from_user.id, message.message_id)
        except Exception as error:
            print(f"Data did not send to admin: {admin}. Error: {error}")
    await message.answer("Tushunarli! Murojaatingizni ko'rib chiqib sizga javob beramiz.\n\nYana murojaatingiz bo'lsa, "
                         "shu yerda yozib qoldirishingiz mumkin.\n\n<b>Biz bilan bo'lganingizdan xursandmiz😊</b>")
