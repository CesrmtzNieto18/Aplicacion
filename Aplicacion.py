import streamlit as st
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Calculadora de Integrales", layout="centered")

st.title("Métodos de Integración Numérica")
st.write("Resuelve ejercicios por Trapecio y Simpson 1/3")

# Entrada de la función
func_input = st.text_input("Define la función f(x) (ejemplo: x**2 + np.sin(x))", "x**2")
a = st.number_input("Límite inferior (a)", value=0.0)
b = st.number_input("Límite superior (b)", value=1.0)
n = st.number_input("Número de intervalos (n)", value=4, step=1)

def f(x):
    # Permite evaluar la cadena de texto como una función matemática
    return eval(func_input)

if st.button("Calcular"):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    # --- Método del Trapecio ---
    trapecio = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])

    # --- Método de Simpson 1/3 ---
    if n % 2 == 0:
        simpson = (h / 3) * (y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2]) + y[-1])
    else:
        simpson = "N/A (n debe ser par para Simpson 1/3)"

    # Mostrar Resultados
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Regla del Trapecio", f"{trapecio:.6f}")
    with col2:
        if isinstance(simpson, str):
            st.error(simpson)
        else:
            st.metric("Regla de Simpson 1/3", f"{simpson:.6f}")

    st.info(f"Tamaño del paso (h) = {h:.4f}")