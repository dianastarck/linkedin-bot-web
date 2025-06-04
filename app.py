
import streamlit as st
import subprocess
import os

st.set_page_config(page_title="LinkedIn AutoBot", layout="centered")
st.title("🤖 LinkedIn Comment Bot")

st.markdown("Pegá aquí la URL de tu publicación en LinkedIn:")

url = st.text_input("URL de la publicación", placeholder="https://www.linkedin.com/feed/update/...")
ejecutar = st.button("🚀 Ejecutar Bot")

if ejecutar:
    if url.strip() == "":
        st.error("⚠️ Pegá una URL válida primero.")
    else:
        with open("input_url.txt", "w") as f:
            f.write(url.strip())

        st.success("✅ URL recibida. Ejecutando el bot...")

        with st.spinner("Procesando..."):
            resultado = subprocess.run(["python3", "bot.py"], capture_output=True, text=True)

        st.success("🎉 ¡Listo! El bot terminó de ejecutarse.")

        files = [f for f in os.listdir() if f.startswith("comentarios_linkedin_") and f.endswith(".xlsx")]
        if files:
            latest = sorted(files)[-1]
            with open(latest, "rb") as file:
                st.download_button("📥 Descargar Excel generado", file, file_name=latest)
        else:
            st.warning("No se generó ningún archivo.")
