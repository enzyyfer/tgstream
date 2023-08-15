from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from WebStreamer.vars import Var
from WebStreamer.bot import StreamBot

@StreamBot.on_message(filters.command(["start", "help"]) & filters.private)
async def start(_, m: Message):
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "You are not in the allowed list of users who can use me. \
            Check <a href='suckmydick'>this link</a> for more info.",
            disable_web_page_preview=True, quote=True
        )
    # Create two buttons
    button1 = InlineKeyboardButton("Update Channel", url="https://t.me/nvreaa")
    button2 = InlineKeyboardButton("Finds Bug?", url="https://t.me/akuniniterjual")
    # Create a keyboard with the buttons
    keyboard = InlineKeyboardMarkup([[button1, button2]])
    # Send the message with the keyboard
    await m.reply(
        f'Hai {m.from_user.mention(style="md")}\nKirim sebuah file saya akan membuatnya menjadi instan link seperti Video dan Audio atau media yang lain.',
        reply_markup=keyboard
    )