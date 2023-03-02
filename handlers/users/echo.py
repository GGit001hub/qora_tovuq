from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes as ct

from loader import dp,bot
from states.kurier import *

kurier = [1173831936,]

# Echo bot




@dp.message_handler(text="yozish",user_id=kurier)
async def kurxona(ms:types.Message):
    await ms.answer("Kimga yozasiz ❓ ID ni kiriting")
    await Kuriers.ids.set()

@dp.message_handler(state=Kuriers.ids)
async def idxona(ms:types.Message,state:FSMContext):
    idn = ms.text
    await state.update_data(ids=idn)
    await ms.answer("Yozishingiz mumkin ✅")
    await Kuriers.xabar.set()



@dp.message_handler(state=Kuriers.xabar)
async def Xbarxona(ms:types.Message,state:FSMContext):
    date = await state.get_data()
    try:
        idn = date.get("ids")
        await bot.send_message(chat_id=idn,text=ms.text)
    except:
        await ms.answer("❌ ID xato ❌")



@dp.message_handler(state=None)
async def bot_echo(ms: types.Message):
    idn = ms.from_user.id
    if idn not in kurier:
        xabar = f"<b>{ms.text}</b>\nID: <code>{ms.from_user.id}</code>\nname: {ms.from_user.full_name}"
        for kr in kurier:
            await bot.send_message(chat_id=kr,text=xabar)


@dp.message_handler(content_types=ct.PHOTO)
async def Rasmxona(ms:types.Message):
    idn = ms.from_user.id
    if idn not in kurier:
        rasm = ms.photo[-1].file_id
        for kr in kurier:
            await bot.send_photo(chat_id=kr,photo=rasm,caption=f"id: {ms.from_user.id}\nname: {ms.from_user.full_name}")


