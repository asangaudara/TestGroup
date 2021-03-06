from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""ð Hi {message.from_user.first_name}!
â¨ I am HÃªlláºÃ¸â  Music Player. 
ð¥³ I can play music in your Telegram Group's Voice Chatð
âï¸ Use these buttons below to know more. ð""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â Source code", url="https://github.com/TheVaders/MusicBot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ð¬ Group", url="https://t.me/hellbot_official_chat"
                    ),
                    InlineKeyboardButton(
                        "Channel ð", url="https://t.me/hellbot_official"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "â Close â", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "**HÃªlláºÃ¸â :** I'm Working!!!\nUse me in Inline to search for a YouTube Video/Music. \n**Happy Streaming**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¶ Search ð¶", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "â Close â", callback_data="close"
                    )
                ]
            ]
        )
    )
