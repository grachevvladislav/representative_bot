from telegram.ext import ContextTypes
from telegram import ReplyKeyboardMarkup, Update
from message import MY_HOBBY, SOURСE_CODE, START_MESSAGE, UNKNOWN_MESSAGES

from constants import keyboard


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


async def voice_command(update: Update, _: ContextTypes.DEFAULT_TYPE):
    text="11111"
    await update.message.reply_text(text)


async def unknown_messages(update: Update, _: ContextTypes.DEFAULT_TYPE):
    """
    Unknown messages handler. Sends a text.
    """
    await update.message.reply_text(UNKNOWN_MESSAGES)
