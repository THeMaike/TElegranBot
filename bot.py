from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)


# -----------------------------
# LISTA DE ITENS PARA PESQUISA
# -----------------------------
ITEMS = [
    "RX 9060 XT 8GB",
    "RX 9060 XT 16GB",
    "RX 7600",
    "RTX 4060",
    "RTX 4070",
    "GTX 1650",
    "RX 580",
    "RTX 4080 SUPER",
]


# -----------------------------
# /start
# -----------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Oi! Sou seu bot de pesquisa de hardware.\n"
        "Digite o nome de uma placa que eu te mostro itens parecidos.\n\n"
        "Exemplo: *4060* ou *RX 580*"
    )


# -----------------------------
# Função de pesquisa
# -----------------------------
def search_items(query: str):
    query = query.lower()
    results = [item for item in ITEMS if query in item.lower()]
    return results


# -----------------------------
# Mensagem comum — pesquisa
# -----------------------------
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    results = search_items(text)

    if not results:
        await update.message.reply_text("❌ Nenhum item encontrado.")
        return

    reply = "🔍 Resultados encontrados:\n\n"
    for r in results:
        reply += f"✅ {r}\n"

    await update.message.reply_text(reply)


# -----------------------------
# MAIN
# -----------------------------
def main():
    token = "8274650004:AAGMJGFwwx3q2Z_fLh5tFWC9NPCWpzsuD_0"

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot iniciado...")
    app.run_polling()


if __name__ == "__main__":
    main()
