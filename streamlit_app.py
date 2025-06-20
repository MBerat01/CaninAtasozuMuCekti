
import streamlit as st
import random
import json
from gtts import gTTS
import os
from utils.analiz import tespit_et

st.set_page_config(page_title="Canın Atasözü mü Çekti?", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: #FF6347;'>📜 Canın Atasözü mü Çekti?</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size:18px; color:#FFA07A;'>🧠 Ne hissettiğini yazmalısın... henüz beynini okuyamıyorum 😅</p>",
    unsafe_allow_html=True
)
st.image("https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif", use_column_width=True)

with open("data/atasozleri.json", "r", encoding="utf-8") as f:
    atasozleri = json.load(f)

gecmis = st.session_state.get("gecmis", {"komik": [], "komik_18": []})

with st.container():
    st.markdown("<hr>", unsafe_allow_html=True)
    secim = st.radio("🎛️ Mod Seçimi:", ["Duyguya Göre", "Komik", "Komik +18"], horizontal=True)
    metin = st.text_input("✍️ Ne hissediyorsun? Yaz bakalım:")

    if st.button("🔮 Atasözü Söyle"):
        if secim == "Duyguya Göre":
            duygu = tespit_et(metin)
            if duygu and duygu in atasozleri:
                secilen = random.choice(atasozleri[duygu])
                st.markdown(f"🧠 **Duygun:** `{duygu}`  
💬 **Atasözü:** *{secilen}*")
                tts = gTTS(text=secilen, lang='tr')
                tts.save("atasozu.mp3")
                audio_file = open("atasozu.mp3", "rb")
                st.audio(audio_file.read(), format="audio/mp3")
            else:
                st.warning("Duygunu algılayamadım, ama yine de güldüreyim 😅")
                adaylar = [a for a in atasozleri["komik"] if a not in gecmis["komik"]]
                if not adaylar:
                    gecmis["komik"] = []
                    adaylar = atasozleri["komik"]
                secilen = random.choice(adaylar)
                gecmis["komik"].append(secilen)
                st.info(secilen)
        elif secim == "Komik +18":
            adaylar = [a for a in atasozleri["komik_18"] if a not in gecmis["komik_18"]]
            if not adaylar:
                gecmis["komik_18"] = []
                adaylar = atasozleri["komik_18"]
            secilen = random.choice(adaylar)
            gecmis["komik_18"].append(secilen)
            st.info(secilen)
        else:
            adaylar = [a for a in atasozleri["komik"] if a not in gecmis["komik"]]
            if not adaylar:
                gecmis["komik"] = []
                adaylar = atasozleri["komik"]
            secilen = random.choice(adaylar)
            gecmis["komik"].append(secilen)
            st.info(secilen)

st.session_state["gecmis"] = gecmis
