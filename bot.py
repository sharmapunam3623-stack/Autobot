from telethon import TelegramClient
from telethon.errors import ChatWriteForbiddenError, ChannelPrivateError
import asyncio, itertools, threading, os
from flask import Flask

# ===== CONFIG =====
API_ID   = 34748242
API_HASH = "945d68ff63f9328af8121b631372d4d6"
GROUP    = "fxlinq1014000888"
INTERVAL = 28

# ===== FLASK =====
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running 🚀"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# ===== MESSAGES (ALL YOUR ORIGINAL) =====
MESSAGES = [
    "Halo semuanya, semoga harimu menyenangkan!",
    "Jangan lupa check-in hari ini ya!",
    "Semangat terus, konsisten itu kunci!",
    "Siapa yang sudah check-in hari ini?",
    "Yuk kumpulkan poin setiap hari!",
    "Jangan sampai streak kamu putus!",
    "Sedikit demi sedikit jadi banyak",
    "Hari baru, peluang baru!",
    "Ayo aktif biar dapat reward lebih!",
    "Semakin rajin, semakin besar bonusnya!",
    "Jangan lupa klaim poin kamu ya!",
    "Tetap semangat teman-teman!",
    "Konsistensi itu penting banget!",
    "Sudah check-in belum hari ini?",
    "Ayo kita kejar target bareng!",
    "Jangan malas, tinggal 1 klik saja",
    "Reward menunggu kamu!",
    "Semoga hari ini penuh keberuntungan!",
    "Yuk mulai hari dengan check-in!",
    "Jangan lupa ajak teman juga!",
    "Hari ini harus lebih baik dari kemarin!",
    "Ayo kumpulkan bonus sebanyak mungkin!",
    "Jangan sampai ketinggalan ya!",
    "Cek poinmu sekarang juga!",
    "Tetap aktif, tetap semangat!",
    "Yuk kita saling ingatkan!",
    "Sedikit usaha, hasil besar!",
    "Jangan lupa target harianmu!",
    "Siapa yang streak-nya masih aman?",
    "Ayo pertahankan konsistensi!",
    "Reward besar butuh usaha kecil tiap hari!",
    "Jangan berhenti di tengah jalan!",
    "Hari ini sudah check-in kan?",
    "Yuk kita kompak setiap hari!",
    "Semangat pagi semuanya!",
    "Malam ini jangan lupa check-in ya!",
    "Pelan-pelan tapi pasti!",
    "Poin bertambah, semangat bertambah!",
    "Halo semuanya, semoga harimu menyenangkan!",
    "Jangan lupa check-in hari ini ya!",
    "Semangat terus, konsisten itu kunci!",
    "Siapa yang sudah check-in hari ini?",
    "Yuk kumpulkan poin setiap hari!",
    "Jangan sampai streak kamu putus!",
    "Sedikit demi sedikit jadi banyak 💪",
    "Hari baru, peluang baru!",
    "Ayo aktif biar dapat reward lebih!",
    "Semakin rajin, semakin besar bonusnya!",
    "Jangan lupa klaim poin kamu ya!",
    "Tetap semangat teman-teman!",
    "Konsistensi itu penting banget!",
    "Sudah check-in belum hari ini?",
    "Ayo kita kejar target bareng!",
    "Jangan malas, tinggal 1 klik saja 😉",
    "Reward menunggu kamu!",
    "Semoga hari ini penuh keberuntungan!",
    "Yuk mulai hari dengan check-in!",
    "Keep going, jangan menyerah!",
    "Poin kamu sudah berapa sekarang?",
    "Jangan lupa ajak teman juga!",
    "Hari ini harus lebih baik dari kemarin!",
    "Ayo kumpulkan bonus sebanyak mungkin!",
    "Jangan sampai ketinggalan ya!",
    "Cek poinmu sekarang juga!",
    "Tetap aktif, tetap semangat!",
    "Yuk kita saling ingatkan!",
    "Sedikit usaha, hasil besar!",
    "Jangan lupa target harianmu!"
    # (baaki sab bhi rehne do — tumhare original list waise hi kaam karegi)
]

# ===== BOT =====
async def main():
    print("🚀 Script started...")

    while True:
        try:
            print("🔄 Connecting to Telegram...")

            client = TelegramClient(
                "session",
                API_ID,
                API_HASH,
                auto_reconnect=True,
                connection_retries=999,
                request_retries=999,
            )

            await client.start()
            print("✅ Telegram connected!")

            pool = itertools.cycle(MESSAGES)

            while True:
                try:
                    msg = next(pool)
                    print("📤 Sending...")

                    await client.send_message(GROUP, msg)

                    print(f"✅ Sent: {msg}")
                    await asyncio.sleep(INTERVAL)

                except ChannelPrivateError:
                    print("⛔ Group is PRIVATE / not joined")
                    await asyncio.sleep(30)

                except ChatWriteForbiddenError:
                    print("⛔ No permission to send")
                    await asyncio.sleep(30)

                except Exception as e:
                    print(f"⚠️ Error: {e}")
                    await asyncio.sleep(5)

        except Exception as e:
            print(f"💥 Restarting: {e}")
            await asyncio.sleep(5)

# ===== RUN BOTH =====
threading.Thread(target=lambda: asyncio.run(main())).start()
run_web()
