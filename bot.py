import logging
import pandas as pd
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from betting_core import suggest_bets
import os

# Configuração de logs
logging.basicConfig(level=logging.INFO)

# Token do Telegram (definido como variável de ambiente no Railway)
TOKEN = os.getenv("BOT_TOKEN")

# Carregar histórico de exemplo
hist = pd.read_csv("matches.csv", parse_dates=['date'])

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Olá! Eu sou seu bot de análise de apostas.\n\n"
        "Use o comando:\n"
        "/analisar TimeA vs TimeB odd_home odd_draw odd_away\n\n"
        "Exemplo:\n"
        "/analisar Flamengo vs Palmeiras 2.10 3.30 3.40"
    )

# Comando /analisar
async def analisar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) != 5:
            await update.message.reply_text("⚠️ Formato correto: /analisar TimeA vs TimeB odd_home odd_draw odd_away")
            return

        home, _, away, odd_home, odd_draw, odd_away = args
        odd_home, odd_draw, odd_away = map(float, [odd_home, odd_draw, odd_away])

        # Criar DataFrame para análise
        upcoming = pd.DataFrame([{
            "date": pd.Timestamp.now(),
            "home_team": home,
            "away_team": away,
            "odd_home": odd_home,
            "odd_draw": odd_draw,
            "odd_away": odd_away,
        }])

        recs = suggest_bets(hist, upcoming)

        if not recs:
            await update.message.reply_text("🚫 Nenhuma aposta de valor encontrada.")
            return

        resposta = "📊 Sugestões de aposta:\n\n"
        for r in recs:
            resposta += (
                f"{r['match']}\n"
                f"→ Mercado: {r['market'].upper()}\n"
                f"Prob: {r['prob']*100:.1f}% | Odd: {r['odd']}\n"
                f"EV: {r['ev']:.2f} | Kelly: {r['kelly_frac']*100:.1f}%\n\n"
            )

        await update.message.reply_text(resposta.strip())

    except Exception as e:
        await update.message.reply_text(f"⚠️ Erro: {e}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("analisar", analisar))
    app.run_polling()

if __name__ == "__main__":
    main()
