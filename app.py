import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ——————————————————————————————
# 1) Configuración de la página
# ——————————————————————————————
st.set_page_config(
    page_title="NextLift IA",
    page_icon="🏋️",
    layout="centered"
)

# ——————————————————————————————
# 2) Mostrar logo
# ——————————————————————————————
THIS_DIR = os.path.dirname(__file__)
logo_path = os.path.join(THIS_DIR, "assets", "logo.png")
st.image(logo_path, use_column_width=True)

# ——————————————————————————————
# 3) Login sencillo con botón
# ——————————————————————————————
if "user" not in st.session_state:
    st.session_state.user = ""

if not st.session_state.user:
    nombre_input = st.text_input("👤 ¿Cómo te llamas?", key="login_input")
    if st.button("Comenzar"):
        if nombre_input.strip():
            st.session_state.user = nombre_input.strip()
            st.success(f"¡Hola, {st.session_state.user}! Vamos a registrar tu entrenamiento.")
        else:
            st.error("Por favor, indica tu nombre.")
    st.stop()

# ——————————————————————————————
# 4) Inicializar estado de wizard y entradas
# ——————————————————————————————
if "step" not in st.session_state:
    st.session_state.step = 1
if "entries" not in st.session_state:
    st.session_state.entries = []

def reset():
    st.session_state.step = 1
    st.session_state.entries = []

# ——————————————————————————————
# 5) Paso 1: Selección de ejercicio
# ——————————————————————————————
if st.session_state.step == 1:
    st.subheader("Paso 1: Elige ejercicio")
    opciones = ["sentadilla", "press banca", "peso muerto", "otro ejercicio"]
    ex = st.selectbox("Ejercicio", opciones)
    if ex == "otro ejercicio":
        ex = st.text_input("Nombre personalizado")
    if st.button("Confirmar ejercicio") and ex:
        st.session_state.exercise = ex
        st.session_state.step = 2

# ——————————————————————————————
# 6) Paso 2: Registro serie a serie
# ——————————————————————————————
elif st.session_state.step == 2:
    st.subheader(f"Paso 2: Registra tu serie de {st.session_state.exercise}")
    with st.form("serie_form"):
        peso = st.number_input("Peso (kg)", min_value=0.0, step=0.5, format="%.1f")
        reps = st.number_input("Reps realizadas", min_value=0, max_value=50, value=8, step=1)
        rpe  = st.number_input("RPE", min_value=0.0, max_value=10.0, value=7.0, step=0.5, format="%.1f")
        submitted = st.form_submit_button("Guardar serie")
    if submitted:
        recomendado = round(peso * 1.02, 1)  # regla +2%
        st.session_state.entries.append({
            "usuario":    st.session_state.user,
            "ejercicio":  st.session_state.exercise,
            "timestamp":  datetime.now(),
            "peso":       peso,
            "reps":       reps,
            "rpe":        rpe,
            "recomendado": recomendado
        })
        st.success(f"Siguiente carga recomendada: {recomendado} kg")

    if st.session_state.entries:
        df_show = pd.DataFrame(st.session_state.entries)
        df_user = df_show[df_show["usuario"] == st.session_state.user].drop(columns="timestamp")
        st.subheader("Tus series registradas")
        st.table(df_user)
        if st.button("Finalizar y ver resumen"):
            st.session_state.step = 3

# ——————————————————————————————
# 7) Paso 3: Resumen y gráfica de progresión
# ——————————————————————————————
elif st.session_state.step == 3:
    st.subheader("Paso 3: Resumen y progresión")
    df = pd.DataFrame(st.session_state.entries)
    df_user = df[df["usuario"] == st.session_state.user].reset_index(drop=True)
    st.table(df_user.drop(columns="timestamp"))

    fig, ax = plt.subplots()
    ax.plot(df_user["recomendado"], marker="o", linestyle="-")
    ax.set_title(f"Progresión recomendada de {st.session_state.user}")
    ax.set_xlabel("Serie")
    ax.set_ylabel("Carga (kg)")
    ax.grid(alpha=0.3)
    st.pyplot(fig)

    if st.button("↺ Empezar de nuevo"):
        reset()

# ——————————————————————————————
# 8) Footer con HTML
# ——————————————————————————————
st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; color:#888;'>
      Developed by <strong>Daniel Eghosa Omoruyi</strong> •
      📧 <a href='mailto:danieleghosa999@gmail.com'>danieleghosa999@gmail.com</a> •
      <a href='https://www.linkedin.com/in/daniel-eghosa-omoruyi/' target='_blank'>
        LinkedIn
      </a>
    </div>
    """,
    unsafe_allow_html=True
)
