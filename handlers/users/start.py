from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from states.kurier import *

kurier = [1173831936,1424712044]


@dp.message_handler(CommandStart(),state=Kuriers.all_states_names,user_id=kurier)
@dp.message_handler(CommandStart())
async def bot_start(message: Message,state:FSMContext):
    if message.from_id not in kurier:
        await message.answer(f"Salom 👋")
        about = message.from_user
        kurier_message = f"👤 User name: {about.full_name}\
            \n🔗 Link: {about.username}\n💡 ID: <code>{about.id}</code>\nlastname: {about.last_name}"
        try:
            for kr in kurier:
                await bot.send_message(kr,kurier_message)
        except:
            pass
    else:
        await message.answer("Salom Kurier. Istagan odamizga yozishingiz mumkin ✅")
        
    await state.finish()




