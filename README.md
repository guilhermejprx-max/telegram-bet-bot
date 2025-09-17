# Telegram Betting Bot 📊

Este bot analisa partidas de futebol usando histórico de resultados, calcula probabilidades (Elo + Poisson) e sugere apostas com base em EV e Critério de Kelly.  

---

## Passo 1 – Criar o bot no Telegram
1. Abra o Telegram e fale com o **BotFather**.  
2. Envie `/newbot` e siga as instruções.  
3. Copie o **TOKEN** fornecido pelo BotFather.

---

## Passo 2 – Preparar o projeto
- Suba este repositório no GitHub.  
- Certifique-se de que contém os arquivos:
  - `bot.py`
  - `betting_core.py`
  - `matches.csv`
  - `requirements.txt`
  - `Procfile`

---

## Passo 3 – Deploy no Railway
1. Crie uma conta em [Railway](https://railway.app) e faça login.  
2. Clique em **New Project → Deploy from GitHub** e conecte este repositório.  
3. Vá em **Settings → Variables** e adicione:
   - `BOT_TOKEN` = seu token do BotFather  
4. Clique em **Deploy**. O bot será executado automaticamente.

---

## Passo 4 – Usar no Telegram
- Abra o bot no Telegram e envie:
