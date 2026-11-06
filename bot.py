import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

ADMIN = "https://t.me/sahilffcreater"
PROOF_CHANNEL = "https://t.me/ffcreatersahil"
QR_FILE = "IMG_20261106_081245.jpg"


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

    if query.data == "service":
        await query.message.reply_text(
            "🔥 FF SERVICES\n\n"
            "Gaming information and general support ke liye admin se contact karein."
        )

    elif query.data == "price":
        await query.message.reply_text(
            "💰 PRICE LIST\n\n"
            "1. Site Registered Problem Fix — ₹399\n"
            "2. Gmail Bind Change / Unbind — ₹499"
        )

    elif query.data == "proof":
        await query.message.reply_text(
            "📢 PROOF CHANNEL\n\n"
            "Join our channel for updates and proofs 👇\n"
            + PROOF_CHANNEL
        )

    elif query.data == "payment":
        try:
            with open(QR_FILE, "rb") as photo:
                await query.message.reply_photo(
                    photo=photo,
                    caption="💳 PAYMENT QR\n\nPayment details admin se confirm karein."
                )
        except FileNotFoundError:
            await query.message.reply_text(
                "Payment QR abhi available nahi hai."
            )


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
