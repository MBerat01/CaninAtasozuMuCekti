import streamlit as st
import random
import json
from gtts import gTTS
import os

# Atasözleri veri kümesi
with open("atasozleri.json", "r", encoding="utf-8") as file:
    atasozleri = json.load(file)

# Duygu kelimeleri
duygular = {
    "mutlu": ["mutluyum", "harika", "çok iyiyim", "sevinçliyim", "keyifliyim"],
    "üzgün": ["üzgünüm", "kötüyüm", "mutsuzum", "ağlıyorum", "moralsizim"],
    "sinirli": ["kızgınım", "öfkeliyim", "sinirliyim", "çıldırıyorum", "tepem attı"],
    "heyecanlı": ["heyecanlıyım", "sabırsızım", "meraklıyım", "can atıyorum"],
    "korkmuş": ["korkuyorum", "endişeliyim", "panik oldum", "ürktüm"]
}

def duygu_tespit(metin):
    metin = metin.lower()
    for duygu, kelimeler in duygular.items():
        if any(k in metin for k in kelimeler):
            return duygu
    return "anlamadım"

st.set_page_config(page_title="Canın Atasözü mü Çekti?", layout="centered")
st.title("📜 Canın Atasözü mü Çekti?")
st.markdown("Duygunu yaz, sana uygun bir atasözü gelsin!")

if "gecmis" not in st.session_state:
    st.session_state.gecmis = {"komik": [], "komik_18": []}

secim = st.radio("🎛️ Mod Seçimi:", ["Duyguya Göre", "Komik", "Komik +18"], horizontal=True)
metin = st.text_input("✍️ Ne hissediyorsun?")

if st.button("🔮 Atasözü Söyle"):
    if secim == "Duyguya Göre":
        duygu = duygu_tespit(metin)
        if duygu in atasozleri:
            secilen = random.choice(atasozleri[duygu])
        else:
            secilen = random.choice(atasozleri["komik"])
            st.warning("Duygun anlaşılamadı, sana komik bir tane seçtim 😅")
        st.success(f"🧠 Duygun: {duygu.capitalize()}")
    elif secim == "Komik":
        kalanlar = [a for a in atasozleri["komik"] if a not in st.session_state.gecmis["komik"]]
        if not kalanlar:
            st.session_state.gecmis["komik"] = []
            kalanlar = atasozleri["komik"]
        secilen = random.choice(kalanlar)
        st.session_state.gecmis["komik"].append(secilen)
    else:
        kalanlar = [a for a in atasozleri["komik_18"] if a not in st.session_state.gecmis["komik_18"]]
        if not kalanlar:
            st.session_state.gecmis["komik_18"] = []
            kalanlar = atasozleri["komik_18"]
        secilen = random.choice(kalanlar)
        st.session_state.gecmis["komik_18"].append(secilen)

    st.markdown(f"📢 **Atasözü:** _{secilen}_")
    try:
        tts = gTTS(text=secilen, lang='tr')
        tts.save("atasozu.mp3")
        st.audio("atasozu.mp3")
    except:
        st.error("Sesli okuma başarısız oldu.")