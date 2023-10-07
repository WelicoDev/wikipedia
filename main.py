import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6313257597:AAFT46-zWMkFZqf9c28fYxdr4bY1ADDii2U'


logging.basicConfig(level=logging.INFO)
wikipedia.set_lang('uz')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("Assalom aleykum !\nMen Wikipedia Bot man !\nKerakli atama yoki ibora nomini kiriting : >>>")
    
@dp.message_handler(commands='help')
async def send_help(message: types.Message):
    await message.reply("Botdagi kamchiliklarni to'g'irlash uchun @welicodev ha yozing !")


@dp.message_handler()
async def send_info(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Ma'lumot topilmadi ! Aniqroq yozing ..")
    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)