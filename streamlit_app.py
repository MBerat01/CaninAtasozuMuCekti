import streamlit as st
import random

# Duygulara göre atasözleri
atasozleri = {
    "mutlu": [
        "Neşeli gönül her yerde bayram eder.",
        "Gülme komşuna, gelir başına.",
        "Ağaç meyvesiyle, insan işiyle övünür.",
        "Bir elin nesi var, iki elin sesi var.",
        "Kendi düşen ağlamaz."
    ],
    "üzgün": [
        "Dertler paylaşıldıkça azalır.",
        "Gönül yarasını hekim saramaz.",
        "Üzüm üzüme baka baka kararır.",
        "Her gecenin bir sabahı vardır.",
        "Ağlarsa anam ağlar, gerisi yalan ağlar."
    ],
    "sinirli": [
        "Öfkeyle kalkan zararla oturur.",
        "Keskin sirke küpüne zarar.",
        "Sakla samanı, gelir zamanı.",
        "Taş yerinde ağırdır.",
        "İt ürür, kervan yürür."
    ],
    "heyecanlı": [
        "İyi şeyler sabırla gelir.",
        "Sakınan göze çöp batar.",
        "Acelem var diyen, yolda kalır.",
        "Azıcık aşım, kaygısız başım.",
        "Bekleyen derviş muradına ermiş."
    ],
    "korkmuş": [
        "Korkunun ecele faydası yok.",
        "Ürkmeyen at yol almaz.",
        "Korkan kaçar, cesur savaşır.",
        "İyi dost kara günde belli olur.",
        "Ateş olmayan yerden duman çıkmaz."
    ],
    "anlamadım": [
        "Ayağını yorganına göre uzat.",
        "Ne oldum dememeli, ne olacağım demeli.",
        "Komşu komşunun külüne muhtaçtır.",
        "Lafla peynir gemisi yürümez.",
        "Taş yerinde ağırdır."
    ]
}

# Duygu kelimeleri
duygular = {
    "mutlu": ["mutluyum", "harika", "çok iyiyim", "sevinçliyim", "keyifliyim"],
    "üzgün": ["üzgünüm", "kötüyüm", "mutsuzum", "ağlıyorum", "moralsizim"],
    "sinirli": ["kızgınım", "öfkeliyim", "sinirliyim", "çıldırıyorum", "tepem attı"],
    "heyecanlı": ["heyecanlıyım", "sabırsızım", "meraklıyım", "can atıyorum"],
    "korkmuş": ["korkuyorum", "endişeliyim", "panik oldum", "ürktüm"]
}

def duygu_tahmin_et(metin):
    metin = metin.lower()
    for duygu, kelimeler in duygular.items():
        if any(kelime in metin for kelime in kelimeler):
            return duygu
    return "anlamadım"

# Streamlit arayüz
st.set_page_config(page_title="Canın Atasözü mü Çekti?", layout="centered")
st.title("📜 Canın Atasözü mü Çekti?")
st.markdown("Duygunu yaz, sana uygun bir atasözü gelsin!")

metin = st.text_input("Bugün nasılsın?")

if st.button("Atasözü Getir"):
    duygu = duygu_tahmin_et(metin)
    secilen = random.choice(atasozleri[duygu])

    if duygu == "anlamadım":
        st.warning("🤖 Ne hissettiğini anlayamadım, beynini henüz okuyamıyorum ama sana bir atasözü bırakayım:")
    else:
        st.success(f"🧠 Duygun: {duygu.capitalize()}")

    st.markdown(f"📢 **Atasözü:** _{secilen}_")