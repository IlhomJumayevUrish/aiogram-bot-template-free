from aiogram import types
from aiogram.types import ContentType
from loader import dp
from pathlib import Path
dawlond_path=Path().joinpath("dawlond","categories")
dawlond_path.mkdir(parents=True,exist_ok=True)
# Echo bot
@dp.message_handler(content_types=ContentType.VIDEO)
async def doc_funck(message: types.Message):
    await message.video.download(destination=dawlond_path)
    await message.reply("Vedio"
                        f" IT={message.video.file_id}")
@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_funck(message: types.Message):
    await message.document.download(destination=dawlond_path)
    await message.reply("Document"
                        f" IT={message.document.file_id}")
@dp.message_handler(content_types=ContentType.PHOTO)
async def doc_funck(message: types.Message):
    await message.photo[-1].download(destination=dawlond_path)
    await message.reply("Photo"
                        f" IT={message.photo[-1].file_id}")

@dp.message_handler(content_types=ContentType.ANY)
async def any_def(message: types.Message):
    await message.reply(message.content_type)