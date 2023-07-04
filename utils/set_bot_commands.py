from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("info_bot", "Bo`t haqida ma`lumot"),
            types.BotCommand("reklama", "Reklama tarqatish"),
            types.BotCommand("countusers", "Bot foydalanuvchilari"),
            types.BotCommand("allusers", "Botdan kimlar foydalanadi"),
        ]
    )
