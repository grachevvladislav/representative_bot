from telegram import Update
from telegram.ext import ContextTypes

from message import MY_HOBBY, SOURСE_CODE, START_MESSAGE, UNKNOWN_MESSAGES


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(START_MESSAGE.format(user.first_name))


async def selfie(update: Update, _: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(photo=open('media/first.jpg', 'rb'))


async def school_photo(update: Update, _: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(photo=open('media/second.jpg', 'rb'))


async def hobby(update: Update, _: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MY_HOBBY)


async def source_code(update: Update, _: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(SOURСE_CODE)


async def what_is_gpt(update: Update, _: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_voice(voice=open('media/what_is_gpt.ogg', 'rb'))


async def sql_nosql(update: Update, _: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_voice(voice=open('media/sql_nosql.ogg', 'rb'))


async def love_story(update: Update, _: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_voice(voice=open('media/love_story.ogg', 'rb'))


async def unknown_messages(update: Update, _: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(UNKNOWN_MESSAGES)
