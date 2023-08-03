from telegram.ext import (ApplicationBuilder, CommandHandler, MessageHandler,
                          filters)

from config import settings
from constants import PATERN
from handlers import (hobby, love_story, school_photo, selfie, source_code,
                      sql_nosql, start, unknown_messages, voice_command,
                      what_is_gpt)


def main():
    app = (
        ApplicationBuilder().token(settings.telegram_token.get_secret_value())
        .build()
    )
    app.add_handlers([
        CommandHandler("start", start),
        CommandHandler("hobby", hobby),
        CommandHandler("voice_gpt", what_is_gpt),
        CommandHandler("voice_sql_nosql", sql_nosql),
        CommandHandler("voice_love_story", love_story),
        CommandHandler("source_code", source_code),
        MessageHandler(filters.Regex(PATERN.format("Моё селфи")), selfie),
        MessageHandler(
            filters.Regex(PATERN.format("Я в старшей школе")), school_photo
        ),
        MessageHandler(filters.VOICE, voice_command),
        MessageHandler(filters.ALL, unknown_messages)
    ])
    app.run_polling()


if __name__ == '__main__':
    main()
