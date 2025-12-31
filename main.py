import telebot
from telebot import types

BOT_TOKEN = "8543718582:AAHGr1Ro-6s2Wbj7SlpVZX5DgIA4DuNeF84"
OWNER_ID = 7743079399

LVL68_IMAGE = "https://t.me/INDRAJITXALL/207"
LVL80_IMAGE = "https://t.me/INDRAJITXALL/221"
QR_IMAGE   = "https://t.me/INDRAJITAPI/112"

bot = telebot.TeleBot(BOT_TOKEN)

# ---------------- START TEXT ----------------

START_TEXT = """
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
🔥🔥 <b>HELLO BROTHER 👋</b> 🔥🔥
<b>━━━━━━━━━━━━━━━━━━━━━━</b>

👑 <b>INDRAJIT 1M</b> 👑
✨ <b>OFFICIAL & TRUSTED NAME</b> ✨

<b>━━━━━━━━━━━━━━━━━━━━━━</b>
🚀 <b>ALL TYPE OF CODES AVAILABLE</b> 🚀
<b>━━━━━━━━━━━━━━━━━━━━━━</b>

✅ <b>ALL NAME CODES</b>
✅ <b>ALL RARE CODES</b>
✅ <b>OLD & UNIQUE IDS</b>
✅ <b>RARE UID WALA ACCOUNT</b>
✅ <b>LIMITED & PREMIUM STOCK</b>

<b>━━━━━━━━━━━━━━━━━━━━━━</b>
💎 <b>SPECIALITY</b> 💎
<b>━━━━━━━━━━━━━━━━━━━━━━</b>

🔥 <b>VERY RARE IDS</b>
🔥 <b>HIGH DEMAND ACCOUNTS</b>
🔥 <b>CLEAN & SAFE</b>
🔥 <b>DIRECT DEALING</b>

<b>━━━━━━━━━━━━━━━━━━━━━━</b>
🛡️ <b>TRUST & SAFETY</b> 🛡️
<b>━━━━━━━━━━━━━━━━━━━━━━</b>

🔒 <b>100% GENUINE</b>
🔒 <b>NO SCAM</b>
🔒 <b>FULL PRIVACY</b>
🔒 <b>TRUSTED SELLER</b>

<b>━━━━━━━━━━━━━━━━━━━━━━</b>
🔥 <b>REMEMBER THE NAME</b> 🔥
👑 <b>INDRAJIT 1M</b> 👑
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
"""

# ---------------- START ----------------

@bot.message_handler(commands=['start'])
def start(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton("🛒 BUY ID", callback_data="buy"),
        types.InlineKeyboardButton("🎮 GUEST ACCOUNT GENERATOR", callback_data="guest"),
        types.InlineKeyboardButton("💳 PAYMENT", callback_data="payment")
    )
    bot.send_message(
        message.chat.id,
        START_TEXT,
        parse_mode="HTML",
        reply_markup=kb
    )

# ---------------- BUY ID ----------------

@bot.callback_query_handler(func=lambda call: call.data == "buy")
def buy(call):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton("🔥 ₹299 – LEVEL 68 ACCOUNT", callback_data="299"),
        types.InlineKeyboardButton("🔥 ₹699 – LEVEL 80 ACCOUNT", callback_data="699")
    )
    bot.send_message(
        call.message.chat.id,
        "<b>SELECT ACCOUNT TYPE</b>",
        parse_mode="HTML",
        reply_markup=kb
    )

# ---------------- 68 LEVEL ----------------

@bot.callback_query_handler(func=lambda call: call.data == "299")
def lvl68(call):
    bot.send_photo(
        call.message.chat.id,
        LVL68_IMAGE,
        caption="""
<b>🔥 LEVEL 68 ACCOUNT 🔥</b>

💰 <b>PRICE:</b> ₹299
✅ CLEAN & SAFE
✅ RARE UID

👉 <b>PAYMENT KARKE TRANSACTION ID SEND KARE</b>

👑 <b>SELLER:</b> INDRAJIT 1M
""",
        parse_mode="HTML"
    )

# ---------------- 80 LEVEL ----------------

@bot.callback_query_handler(func=lambda call: call.data == "699")
def lvl80(call):
    bot.send_photo(
        call.message.chat.id,
        LVL80_IMAGE,
        caption="""
<b>🔥 LEVEL 80 ACCOUNT 🔥</b>

💰 <b>PRICE:</b> ₹699
✅ OLD ID
✅ HIGH DEMAND
✅ PREMIUM ACCOUNT

👉 <b>PAYMENT KARKE TRANSACTION ID SEND KARE</b>

👑 <b>SELLER:</b> INDRAJIT 1M
""",
        parse_mode="HTML"
    )

# ---------------- GUEST ACCOUNT ----------------

@bot.callback_query_handler(func=lambda call: call.data == "guest")
def guest(call):
    text = """
<b>GUEST ACCOUNT GEN BOT CODE</b>

<b>RS = 89</b>

<b>👇 COPY KARKE USE KARE 👇</b>
"""
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("⬇️ DOWNLOAD", url="https://example.com"))
    bot.send_message(call.message.chat.id, text, parse_mode="HTML", reply_markup=kb)

# ---------------- PAYMENT ----------------

@bot.callback_query_handler(func=lambda call: call.data == "payment")
def payment(call):
    bot.send_photo(
        call.message.chat.id,
        QR_IMAGE,
        caption="<b>SCAN & PAY ONLY\nENTER TRANSACTION ID</b>",
        parse_mode="HTML"
    )
    bot.register_next_step_handler(call.message, get_txn)

def get_txn(message):
    txn = message.text
    bot.send_message(
        OWNER_ID,
        f"""
<b>💳 NEW PAYMENT RECEIVED</b>

👤 <b>USER:</b> @{message.from_user.username}
🆔 <b>USER ID:</b> {message.from_user.id}
💰 <b>TXN ID:</b> {txn}
""",
        parse_mode="HTML"
    )
    bot.send_message(
        message.chat.id,
        "<b>✅ PAYMENT RECEIVED\nOWNER WILL CONTACT YOU</b>",
        parse_mode="HTML"
    )

# ---------------- OWNER PANEL ----------------

@bot.message_handler(commands=['owner'])
def owner_panel(message):
    if message.from_user.id == OWNER_ID:
        msg = bot.send_message(message.chat.id, "<b>ENTER USERNAME (without @)</b>", parse_mode="HTML")
        bot.register_next_step_handler(msg, owner_username)

def owner_username(message):
    username = message.text
    msg = bot.send_message(message.chat.id, "<b>ENTER MESSAGE</b>", parse_mode="HTML")
    bot.register_next_step_handler(msg, owner_message, username)

def owner_message(message, username):
    bot.send_message(
        f"@{username}",
        f"""
<b>ID & PASSWORD DETAILS</b>

👑 <b>SELLER:</b> INDRAJIT 1M 👑
""",
        parse_mode="HTML"
    )

# ---------------- RUN ----------------

bot.infinity_polling()