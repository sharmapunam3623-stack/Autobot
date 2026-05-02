from telethon import TelegramClient
from telethon.errors import ChatWriteForbiddenError, ChannelPrivateError
import asyncio, itertools, threading, os
from flask import Flask

API_ID   = 34748242
API_HASH = "945d68ff63f9328af8121b631372d4d6"
GROUP    = "fxlinq1014000888"
INTERVAL = 28

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running 🚀"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# 👇 PASTE ALL YOUR 261 MESSAGES HERE
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
    "Jangan lupa target harianmu!",
    "Selamat pagi, semoga harimu menyenangkan dan penuh berkah.",
    "Terima kasih atas bantuan dan dukunganmu selama ini.",
    "Maaf telah membuatmu menunggu terlalu lama.",
    "Aku sangat menghargai keberadaanmu dalam hidupku.",
    "Semoga mimpi-mimpimu segera menjadi kenyataan.",
    "Jangan menyerah, setiap perjuangan pasti ada hasilnya.",
    "Kamu adalah alasan aku terus tersenyum setiap hari.",
    "Bersabarlah, waktu akan menjawab semua pertanyaanmu.",
    "Aku bangga dengan semua yang telah kamu capai.",
    "Tolong jaga kesehatanmu dengan baik.",
    "Hidupmu sangat berharga, jangan pernah melupakannya.",
    "Kita bisa melewati masa sulit ini bersama-sama.",
    "Setiap hari adalah kesempatan baru untuk menjadi lebih baik.",
    "Percayalah pada kemampuanmu sendiri.",
    "Aku selalu ada untukmu, kapanpun kamu membutuhkanku.",
    "Kebaikanmu telah menyentuh hati banyak orang.",
    "Jangan lupa makan dan istirahat yang cukup.",
    "Kamu lebih kuat dari yang kamu kira.",
    "Hari ini pasti lebih baik dari kemarin.",
    "Terima kasih sudah menjadi temanku yang setia.",
    "Setiap langkah kecil tetap membawamu maju ke depan.",
    "Jangan biarkan ketakutan menghalangi impianmu.",
    "Kamu membuat dunia ini menjadi tempat yang lebih baik.",
    "Semoga perjalananmu hari ini lancar dan menyenangkan.",
    "Aku selalu mendoakan yang terbaik untukmu.",
    "Tetaplah semangat meskipun rintangan terasa berat.",
    "Senyummu adalah kekuatan terbesar yang kamu miliki.",
    "Jangan ragu untuk meminta bantuan saat kamu membutuhkannya.",
    "Setiap kegagalan adalah pelajaran berharga dalam hidupmu.",
    "Cinta dan kasih sayang selalu menyertaimu.",
    "Aku percaya kamu bisa melakukan hal-hal luar biasa.",
    "Waktu terbaik untuk memulai adalah sekarang.",
    "Keberhasilan sejati dimulai dari keberanian untuk mencoba.",
    "Jangan lupa bersyukur atas semua yang kamu miliki.",
    "Harapan adalah cahaya di ujung lorong yang gelap.",
    "Kamu tidak sendirian dalam perjalanan hidupmu ini.",
    "Setiap detik kehidupan adalah anugerah yang patut disyukuri.",
    "Kerendahan hati adalah kunci menuju kebijaksanaan sejati.",
    "Persahabatan yang tulus lebih berharga dari harta benda.",
    "Jangan biarkan masa lalu menentukan masa depanmu.",
    "Keberanian bukan berarti tidak takut, tapi tetap maju meski takut.",
    "Kamu berhak mendapatkan kebahagiaan yang sesungguhnya.",
    "Setiap orang punya ceritanya masing-masing, hargailah itu.",
    "Kata-kata yang baik dapat mengubah hari seseorang.",
    "Jadilah versi terbaik dari dirimu sendiri.",
    "Cinta tidak membutuhkan kata-kata, cukup dengan tindakan.",
    "Rumah bukan hanya tempat tinggal, tapi di mana hati berada.",
    "Kesederhanaan adalah bentuk kemewahan yang sesungguhnya.",
    "Alam mengajarkan kita tentang ketenangan dan kesabaran.",
    "Musik adalah bahasa yang semua orang bisa pahami.",
    "Buku adalah jendela menuju dunia yang tak terbatas.",
    "Kreativitas tumbuh subur di dalam keheningan.",
    "Bermimpilah besar, tapi mulailah dari langkah kecil.",
    "Kerja keras dan ketekunan selalu membuahkan hasil.",
    "Kejujuran adalah fondasi dari kepercayaan yang sejati.",
    "Tersenyumlah, karena senyum bisa menular kepada orang lain.",
    "Keluarga adalah harta yang paling berharga di dunia.",
    "Masa muda adalah waktu untuk belajar dan berkembang.",
    "Setiap matahari terbenam membawa janji fajar yang baru.",
    "Hormatilah orang tua, karena mereka adalah segalanya bagimu.",
    "Persahabatan sejati tahan terhadap badai kehidupan.",
    "Doa adalah kekuatan yang melampaui segala batas.",
    "Ilmu pengetahuan adalah senjata paling ampuh di dunia.",
    "Jadilah pemimpin yang menginspirasi, bukan yang menakut-nakuti.",
    "Kedamaian dimulai dari dalam diri sendiri.",
    "Setiap kata yang kita ucapkan punya kekuatan tersendiri.",
    "Anak-anak mengajarkan kita melihat dunia dengan mata segar.",
    "Pengorbanan tulus adalah bentuk cinta yang paling murni.",
    "Waktu yang berlalu tidak bisa dikembalikan, manfaatkan sebaik-baiknya.",
    "Kebersamaan adalah sumber kekuatan yang tak ternilai.",
    "Dengarkan dengan hatimu, bukan hanya dengan telingamu.",
    "Setiap pagi membawa semangat dan energi yang baru.",
    "Kegigihan adalah bahan bakar menuju kesuksesan abadi.",
    "Rasa syukur membuka pintu kebahagiaan yang lebih luas.",
    "Jangan menghakimi orang lain sebelum memahami ceritanya.",
    "Kepercayaan dibangun perlahan tapi bisa hancur seketika.",
    "Setiap pertemuan membawa pelajaran yang tak terduga.",
    "Belas kasihan adalah kekuatan, bukan kelemahan.",
    "Hidup adalah perjalanan, bukan sekadar tujuan akhir.",
    "Keberanian untuk berubah adalah langkah awal menuju pertumbuhan.",
    "Cintailah dirimu sendiri sebelum mencintai orang lain.",
    "Rintangan terbesar sering kali ada di dalam pikiran kita sendiri.",
    "Setiap orang berhak mendapat kesempatan kedua.",
    "Ketenangan pikiran lebih berharga dari kekayaan manapun.",
    "Jadikan setiap hari pengalaman belajar yang berharga.",
    "Mimpi yang besar membutuhkan usaha yang besar pula.",
    "Bantulah sesama tanpa mengharapkan imbalan apapun.",
    "Bersikaplah baik, karena semua orang sedang berjuang.",
    "Ide-ide besar sering lahir dari keberanian untuk berbeda.",
    "Masa depan milik mereka yang mempersiapkan diri hari ini.",
    "Kesetiaan adalah mahkota karakter yang sesungguhnya.",
    "Seorang teman sejati hadir di saat suka maupun duka.",
    "Kebebasan sejati lahir dari tanggung jawab yang diemban.",
    "Hidup tanpa tujuan bagaikan kapal tanpa kemudi.",
    "Pengalaman adalah guru terbaik yang pernah ada.",
    "Kesuksesan bukan soal seberapa cepat, tapi seberapa tekun.",
    "Cinta yang tulus tidak memerlukan pengakuan dari siapapun.",
    "Mulailah harimu dengan rasa syukur yang tulus.",
    "Jangan biarkan kegagalan mendefinisikan siapa dirimu.",
    "Dalam setiap kesulitan selalu tersimpan peluang yang berharga.",
    "Kata maaf yang tulus bisa menyembuhkan luka yang dalam.",
    "Jadilah cahaya di tengah kegelapan orang-orang di sekitarmu.",
    "Setiap manusia memiliki potensi tak terbatas untuk berkembang.",
    "Ketulusan hati lebih indah dari penampilan yang sempurna.",
    "Pikiran positif menciptakan kehidupan yang lebih bermakna.",
    "Berjuanglah untuk hal-hal yang benar-benar penting bagimu.",
    "Ketabahan adalah bunga yang mekar di tanah yang keras.",
    "Perdamaian adalah warisan terbaik yang kita tinggalkan.",
    "Setiap kisah hidup layak untuk diceritakan dengan bangga.",
    "Hormatilah perbedaan, karena di situlah keindahan sejati.",
    "Jadilah pendengar yang baik bagi orang-orang di sekitarmu.",
    "Kekuatan sejati berasal dari dalam hati yang lapang.",
    "Setiap tetes keringat kerja keras pasti ada balasannya.",
    "Bergegaslah berbuat baik sebelum kesempatan berlalu.",
    "Kehangatan persahabatan menguatkan kita di hari-hari berat.",
    "Jadikan kritikan sebagai batu loncatan menuju perbaikan.",
    "Setiap manusia unik dan berharga dengan caranya sendiri.",
    "Kebaikan hati tidak pernah sia-sia walau sekecil apapun.",
    "Tumbuhkan empati, karena dunia sangat membutuhkannya.",
    "Hidup yang bermakna bukan dinilai dari lamanya, tapi dalamnya.",
    "Setiap hari, cobalah menjadi orang yang lebih baik dari kemarin.",
    "Jangan pernah menyepelekan dampak dari satu kebaikan kecil.",
    "Kebijaksanaan datang dari pengalaman yang direnungkan dengan matang.",
    "Jadilah teladan yang menginspirasi generasi-generasi berikutnya.",
    "Rasa ingin tahu adalah mesin penggerak kemajuan manusia.",
    "Memaafkan bukan berarti melupakan, tapi membebaskan dirimu sendiri.",
    "Setiap langkah maju dimulai dari keputusan untuk bangkit.",
    "Alam semesta mendukung mereka yang berani bermimpi besar.",
    "Kasih sayang yang tulus tidak mengenal batas apapun.",
    "Bersyukurlah atas hari-hari biasa, karena itulah kehidupan.",
    "Setiap buku yang dibaca membuka cakrawala pikiran yang baru.",
    "Jangan biarkan rasa takut mencuri mimpi-mimpimu.",
    "Keberhasilan adalah hasil dari pilihan dan dedikasi setiap hari.",
    "Jadikan kesalahan sebagai bahan bakar untuk tumbuh lebih kuat.",
    "Dunia berubah melalui tangan mereka yang tidak menyerah.",
    "Cinta yang murni tumbuh dari penerimaan yang tulus.",
    "Setiap tantangan adalah undangan untuk menemukan kekuatan baru.",
    "Orang bijak belajar dari kesalahan orang lain dan dirinya sendiri.",
    "Kejujuran mungkin menyakitkan, tapi selalu lebih baik dari kebohongan.",
    "Setiap momen bersama orang tersayang adalah harta tak ternilai.",
    "Jadikan hidupmu cerita yang layak untuk diceritakan dengan bangga.",
    "Semangat yang membara membuat hal mustahil menjadi mungkin.",
    "Keberanian untuk jujur adalah bentuk cinta yang paling nyata.",
    "Hari-hari sulit mengajarkan kita menghargai hari-hari yang indah.",
    "Langit malam penuh bintang mengingatkan kita tentang keajaiban.",
    "Setiap generasi bertanggung jawab untuk dunia yang lebih baik.",
    "Hormatilah waktu orang lain seperti kamu menghargai waktumu sendiri.",
    "Kreativitas adalah kemampuan manusia yang tak mengenal batas.",
    "Kata-kata penyemangat bisa mengubah arah perjalanan seseorang.",
    "Kepercayaan diri bukan tentang sempurna, tapi berani menjadi dirimu.",
    "Setiap pagi adalah halaman baru dalam buku kehidupanmu.",
    "Jangan bandingkan perjalananmu dengan perjalanan orang lain.",
    "Ketulusan dalam berbuat baik adalah investasi terbaik dalam hidup.",
    "Setiap orang yang kita temui mengajarkan sesuatu yang berharga.",
    "Kekuatan komunitas lebih besar dari kekuatan individu manapun.",
    "Jadikan kerendahan hati sebagai kompas dalam setiap tindakanmu.",
    "Belajarlah dari alam tentang cara menghadapi perubahan dengan anggun.",
    "Setiap impian besar pernah dimulai sebagai pikiran kecil.",
    "Jangan biarkan opini orang lain mendefinisikan nilai dirimu.",
    "Kesehatan mental sama pentingnya dengan kesehatan fisik.",
    "Cinta diri sendiri adalah fondasi dari semua hubungan yang sehat.",
    "Setiap pilihan membawa konsekuensi, jadilah bijak dalam memilih.",
    "Waktu bersama orang-orang yang kita cintai tidak pernah terbuang.",
    "Jadilah bagian dari solusi, bukan bagian dari masalah.",
    "Kepedulian terhadap sesama adalah inti dari kemanusiaan sejati.",
    "Setiap senyum yang kamu berikan kembali kepadamu dengan cara berbeda.",
    "Proses belajar tidak pernah berhenti selama kita masih hidup.",
    "Ketekunan kecil setiap hari menghasilkan perubahan besar dari waktu.",
    "Jadilah orang yang membuat orang lain merasa lebih baik.",
    "Setiap hubungan membutuhkan pengertian, kepercayaan, dan komunikasi.",
    "Daya juang adalah bahan bakar yang tidak pernah habis dalam dirimu.",
    "Nilai seseorang bukan diukur dari apa yang dimilikinya.",
    "Setiap hari adalah peluang untuk membuat perbedaan nyata di dunia.",
    "Kesederhanaan hidup membawa ketenangan yang jarang ditemukan.",
    "Jadikan setiap perpisahan sebagai motivasi untuk bertemu kembali.",
    "Keberanian untuk bermimpi adalah langkah pertama menuju kenyataan.",
    "Perubahan dimulai dari keputusan kecil yang dibuat setiap harinya.",
    "Setiap tawa yang dibagikan mempererat ikatan yang tak terlihat.",
    "Jadilah penuh syukur atas hal-hal kecil yang sering terlupakan.",
    "Kamu adalah karya terbaik yang terus menyempurnakan dirinya sendiri.",
    "Semoga setiap doamu dijawab pada waktu yang paling tepat.",
    "Kepercayaan adalah jembatan yang menghubungkan hati ke hati.",
    "Setiap cerita sedih punya bab berikutnya yang penuh harapan.",
    "Jadilah teman yang hadir bukan hanya di saat senang saja.",
    "Kekuatan doa melampaui semua logika dan pemahaman manusia.",
    "Setiap langkahmu ke depan adalah kemenangan atas rasa takutmu.",
    "Hidup adalah tentang memberi, bukan hanya tentang menerima.",
    "Keindahan sejati terletak pada hati yang penuh kebaikan.",
    "Setiap mimpi yang kamu miliki layak untuk diperjuangkan sungguh-sungguh.",
    "Jangan pernah meragukan kekuatan cinta yang tulus dan ikhlas.",
    "Bersama kita lebih kuat, bersama kita bisa melampaui segalanya.",
    "Setiap hari adalah hadiah, itulah mengapa disebut hari ini.",
    "Jadikan hidupmu cerita yang menginspirasi jutaan orang lainnya.",
]

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
                    print("⛔ Group is PRIVATE")
                    await asyncio.sleep(30)

                except ChatWriteForbiddenError:
                    print("⛔ No permission")
                    await asyncio.sleep(30)

                except Exception as e:
                    print(f"⚠️ Error: {e}")
                    await asyncio.sleep(5)

        except Exception as e:
            print(f"💥 Restarting: {e}")
            await asyncio.sleep(5)

threading.Thread(target=lambda: asyncio.run(main())).start()
run_web()
