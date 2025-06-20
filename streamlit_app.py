
import streamlit as st
import random
from gtts import gTTS
import json
import os

# JSON'dan atasözleri yükle
with open("atasozleri.json", "r", encoding="utf-8") as f:
    atasozleri = json.load(f)

# Duygu kelimeleri
duygular = {
    "mutlu": ["mutluyum", "harika", "çok iyiyim", "sevinçliyim", "keyifliyim"],
    "üzgün": ["üzgünüm", "kötüyüm", "mutsuzum", "ağlıyorum", "moralsizim"],
    "sinirli": ["kızgınım", "öfkeliyim", "sinirliyim", "çıldırıyorum", "tepem attı"],
    "heyecanlı": ["heyecanlıyım", "sabırsızım", "meraklıyım", "can atıyorum"],
    "korkmuş": ["korkuyorum", "endişeliyim", "panik oldum", "ürktüm"]
}

# Duyguyu metinden tahmin et
def duygu_tahmin_et(metin):
    metin = metin.lower()
    for duygu, kelimeler in duygular.items():
        if any(kelime in metin for kelime in kelimeler):
            return duygu
    return "anlamadım"

# Geçmişi saklamak için session_state
if "gecmis" not in st.session_state:
    st.session_state["gecmis"] = {"komik": [], "komik_18": []}

st.set_page_config(page_title="Canın Atasözü mü Çekti?", layout="centered")
st.title("📜 Canın Atasözü mü Çekti?")

st.markdown("🎯 **Duygunu ya da hissettiklerini yaz, sana uygun bir atasözü gelsin!**")
st.markdown("<hr>", unsafe_allow_html=True)

secim = st.radio("🎛️ Mod Seçimi:", ["Duyguya Göre", "Komik", "Komik +18"], horizontal=True)
metin = st.text_input("✍️ Bugünkü ruh halin?")

if st.button("🔮 Atasözü Söyle"):
    gecmis = st.session_state["gecmis"]

    if secim == "Duyguya Göre":
        duygu = duygu_tahmin_et(metin)
        if duygu in atasozleri:
            secilen = random.choice(atasozleri[duygu])
            st.success(f"🧠 Duygun: `{duygu}`")
        else:
            duygu = "anlamadım"
            secilen = random.choice(atasozleri[duygu])
            st.warning("🤖 Ne hissettiğini anlayamadım, beynini henüz okuyamıyorum ama sana bir atasözü bırakayım:")

    elif secim == "Komik":
        adaylar = [a for a in atasozleri["komik"] if a not in gecmis["komik"]]
        if not adaylar:
            gecmis["komik"] = []
            adaylar = atasozleri["komik"]
        secilen = random.choice(adaylar)
        gecmis["komik"].append(secilen)

    else:  # Komik +18
        adaylar = [a for a in atasozleri["komik_18"] if a not in gecmis["komik_18"]]
        if not adaylar:
            gecmis["komik_18"] = []
            adaylar = atasozleri["komik_18"]
        secilen = random.choice(adaylar)
        gecmis["komik_18"].append(secilen)

    # Atasözünü göster
    st.markdown(f"📢 **Atasözü:** _{secilen}_")

    # Sesli oku
    tts = gTTS(text=secilen, lang='tr')
    tts.save("atasozu.mp3")
    st.audio("atasozu.mp3")

    st.session_state["gecmis"] = gecmis
