
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

ADMIN = "https://t.me/sahilffcreater"

async def start(update: Update, context):
    keyboard = [
        [
            InlineKeyboardButton("🔥 FF SERVICES", callback_data="service"),
            InlineKeyboardButton("💰 PRICE LIST", callback_data="price")
        ],
        [
            InlineKeyboardButton("📢 PROOF CHANNEL", callback_data="proof"),
            InlineKeyboardButton("💳 PAYMENT", callback_data="payment")
        ],
        [
            InlineKeyboardButton("👨‍💻 CONTACT ADMIN", url=ADMIN)
        ]
    ]

    await update.message.reply_text(
        "👑 Welcome to FF SERVICE BOT!\n\nChoose an option below 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context):
    query = update.callback_query
    await query.answer()

    messages = {
        "service": "🔥 FF SERVICES\n\nGaming information and general support ke liye admin se contact karein.",
        "price": "💰 PRICE LIST\n\nLatest price details ke liye admin se contact karein.",
        "proof": "📢 PROOF CHANNEL\n\nProof channel link jald add hoga."
    }

    if query.data == "payment":
        try:
            with open("payment_qr.png", "rb") as photo:
                await query.message.reply_photo(
                    photo=photo,
                    caption="💳 PAYMENT QR\n\nPayment se pehle admin se details confirm karein."
                )
        except FileNotFoundError:
            await query.message.reply_text("Payment QR abhi available nahi hai.")
    else:
        await query.message.reply_text(messages[query.data])

def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN secret is missing!")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("Bot is running!")
    app.run_polling()

if __name__ == "__main__":
    main()

