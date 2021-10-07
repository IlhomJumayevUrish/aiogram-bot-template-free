from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.reply("message.text,message.text \n"
                        f"Ok {45}")
    await message.answer("Ok")