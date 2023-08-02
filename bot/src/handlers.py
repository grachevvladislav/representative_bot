import os

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from constants import keyboard, voice_commands
from message import (MY_HOBBY, SOURСE_CODE, START_MESSAGE, TOO_LONG_MESSAGE,
                     UNKNOWN_MESSAGES, ERROR_MESSAGE)
from voice_to_text import recognize


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE):
    """/start command handler. Sends a welcome message and a keyboard."""
    user = update.effective_user
    await update.message.reply_html(
        START_MESSAGE.format(user.first_name),
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            one_time_keyboard=False,
            resize_keyboard=True
        )
    )


async def selfie(update: Update, _: ContextTypes.DEFAULT_TYPE):
    """
    'My selfie' button handler. Sends a photo.
    """
    await update.message.reply_photo(photo=open('media/first.jpg', 'rb'))


async def school_photo(update: Update, _: ContextTypes.DEFAULT_TYPE):
    """
    'School selfie' button handler. Sends a photo.
    """
    await update.message.reply_photo(photo=open('media/second.jpg', 'rb'))


async def hobby(update: Update, _: ContextTypes.DEFAULT_TYPE):
    """
    /hobby command handler. Sends a text.
    """
    await update.message.reply_text(MY_HOBBY)


async def source_code(update: Update, _: ContextTypes.DEFAULT_TYPE):
    """
    /source_code command handler. Sends a text.
    """
    await update.message.reply_text(SOURСE_CODE)


async def what_is_gpt(update: Update, _: ContextTypes.DEFAULT_TYPE):
    """
    /voice_gpt command handler. Sends a voice.
    """
    await update.message.reply_voice(voice=open('media/what_is_gpt.ogg', 'rb'))


async def sql_nosql(update: Update, _: ContextTypes.DEFAULT_TYPE):
    """
    /voice_sql_nosql command handler. Sends a voice.
    """
    await update.message.reply_voice(voice=open('media/sql_nosql.ogg', 'rb'))


async def love_story(update: Update, _: ContextTypes.DEFAULT_TYPE):
    """
    /voice_love_story command handler. Sends a voice.
    """
    await update.message.reply_voice(voice=open('media/love_story.ogg', 'rb'))


async def voice_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Accepts voice commands and calls handler.
    """
    if update.message.voice.duration > 15:
        await update.message.reply_text(TOO_LONG_MESSAGE)

    filename = update.message.voice.file_id + ".ogg"
    file = await update.message.effective_attachment.get_file()
    await file.download_to_drive(filename)
    text = await recognize(filename)
    os.remove(filename)

    if text == "":
        await update.message.reply_text(ERROR_MESSAGE)
    handler = globals().get(voice_commands.get(text.lower()))
    if handler and callable(handler):
        await handler(update, context)
    else:
        await update.message.reply_text(UNKNOWN_MESSAGES)


async def unknown_messages(update: Update, _: ContextTypes.DEFAULT_TYPE):
    """
    Unknown messages handler. Sends a text.
    """
    await update.message.reply_text(UNKNOWN_MESSAGES)
