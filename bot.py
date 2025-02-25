from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7773863105:AAF0aHaAnyuiiswq7kZJHGfaGVQYX3WL-pI"  # Replace with your actual bot token

# Start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hey this is a bot devoleped by @h3lixx for "CLAN GOTEN"MEMBERS")

# Reply to messages
async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(update.message.text)

def main():
    app = Application.builder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
