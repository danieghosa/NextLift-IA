import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 0) Configuración de página
st.set_page_config(page_title="NextLift IA", layout="centered")
st.image("logo.png", use_column_width=True)

# 1) Logo
st.image("logo.png", width=200)
st.title("NextLift IA")

# Inicializamos estado
if "step" not in st.session_state:
    st.session_state.step = 1
if "exercise" not in st.session_state:
    st.session_state.exercise = None
if "entries" not in st.session_state:
    st.session_state.entries = []

# Función para reiniciar todo
def reset():
    st.session_state.step = 1
    st.session_state.exercise = None
    st.session_state.entries = []

# 2) Paso 1: seleccionar ejercicio
if st.session_state.step == 1:
    st.subheader("Paso 1: Elige ejercicio")
    ex = st.selectbox("Ejercicio", ["sentadilla","press banca","peso muerto","otro ejercicio"])
    if ex == "otro ejercicio":
        ex = st.text_input("Nombre de ejercicio personalizado")
    if st.button("Confirmar ejercicio"):
        if ex:
            st.session_state.exercise = ex
            st.session_state.step = 2

# 3) Paso 2: introducir serie a serie
elif st.session_state.step == 2:
    st.subheader(f"Paso 2: Registra tu serie de {st.session_state.exercise}")
    with st.form("serie_form"):
        peso = st.number_input("Peso (kg)", min_value=0.0, step=0.5, format="%.1f")
        reps = st.number_input("Reps realizadas", min_value=0, max_value=20, value=8, step=1)
        rpe  = st.number_input("RPE", min_value=0.0, max_value=10.0, value=7.0, step=0.5, format="%.1f")
        submitted = st.form_submit_button("Guardar serie")
    if submitted:
        # calcular recomendación (+2 % de la carga de esta serie)
        recomendado = round(peso * 1.02, 1)
        # almacenar
        st.session_state.entries.append({
            "timestamp": datetime.now(),
            "ejercicio": st.session_state.exercise,
            "peso": peso,
            "reps": reps,
            "rpe": rpe,
            "recomendado": recomendado
        })
        st.success(f"Siguiente carga recomendada: {recomendado} kg")
    # mostrar tablas y botón de terminar
    if st.session_state.entries:
        st.subheader("Series registradas")
        df = pd.DataFrame(st.session_state.entries).drop(columns="timestamp")
        st.table(df)
        # botón para pasar al resumen final
        if st.button("Finalizar y ver resumen"):
            st.session_state.step = 3

# 4) Paso 3: resumen y gr����fica
elif st.session_state.step == 3:
    st.subheader("Paso 3: Resumen y progresión")
    df = pd.DataFrame(st.session_state.entries)
    st.table(df.drop(columns="timestamp"))
    # gráfica de evolución de peso
    fig, ax = plt.subplots()
    ax.plot(df["recomendado"].reset_index(drop=True), marker="o", linestyle="-")
    ax.set_title(f"Progresión recomendada para {st.session_state.exercise}")
    ax.set_xlabel("Serie")
    ax.set_ylabel("Carga (kg)")
    st.pyplot(fig)
    # opción de reiniciar
    st.button("↺ Comenzar de nuevo", on_click=reset)

st.sidebar.markdown("## About")
st.sidebar.markdown("**NextLift IA** by Daniel Eghosa Omoruyi\n\n"
                    "🚀 Founder @ NextLift Technologies\n\n"
                    "✉️ contacto@nextlift.ai\n\n"
                    "[GitHub](https://github.com/danieghosa) • "
                    "[LinkedIn](https://www.linkedin.com/in/danieghosa)")
