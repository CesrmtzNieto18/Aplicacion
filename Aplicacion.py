import streamlit as st
import numpy as np

# Configuración
st.set_page_config(page_title="Métodos Numéricos", layout="centered")

st.title("Calculadora de Métodos Numéricos")

# =========================
# MENÚ
# =========================
metodo = st.selectbox(
    "Selecciona un método",
    [
        "Integración - Trapecio",
        "Integración - Simpson 1/3",
        "Integración - Simpson 3/8",
        "Diferenciación Numérica",
        "Interpolación Lineal"
    ]
)

# =========================
# FUNCIÓN
# =========================
func_input = st.text_input(
    "Define la función f(x)",
    "x**2"
)

def f(x):
    return eval(func_input)

# =========================
# INTEGRACIÓN
# =========================
if "Integración" in metodo:

    a = st.number_input("Límite inferior (a)", value=0.0)
    b = st.number_input("Límite superior (b)", value=1.0)
    n = st.number_input("Número de intervalos (n)", value=4, step=1)

    if st.button("Calcular"):

        h = (b - a) / n
        x = np.linspace(a, b, n + 1)
        y = f(x)

        # =========================
        # TRAPECIO
        # =========================
        if metodo == "Integración - Trapecio":

            resultado = (h / 2) * (
                y[0] + 2 * sum(y[1:-1]) + y[-1]
            )

            st.success(f"Resultado Trapecio = {resultado:.6f}")

        # =========================
        # SIMPSON 1/3
        # =========================
        elif metodo == "Integración - Simpson 1/3":

            if n % 2 == 0:

                resultado = (h / 3) * (
                    y[0]
                    + 4 * sum(y[1:-1:2])
                    + 2 * sum(y[2:-2:2])
                    + y[-1]
                )

                st.success(f"Resultado Simpson 1/3 = {resultado:.6f}")

            else:
                st.error("n debe ser par")

        # =========================
        # SIMPSON 3/8
        # =========================
        elif metodo == "Integración - Simpson 3/8":

            if n % 3 == 0:

                suma = 0

                for i in range(1, n):

                    if i % 3 == 0:
                        suma += 2 * y[i]
                    else:
                        suma += 3 * y[i]

                resultado = (3 * h / 8) * (
                    y[0] + suma + y[-1]
                )

                st.success(f"Resultado Simpson 3/8 = {resultado:.6f}")

            else:
                st.error("n debe ser múltiplo de 3")

        st.info(f"Tamaño del paso h = {h:.4f}")

# =========================
# DIFERENCIACIÓN
# =========================
elif metodo == "Diferenciación Numérica":

    x0 = st.number_input("Valor de x", value=1.0)
    h = st.number_input("Valor de h", value=0.1)

    if st.button("Calcular"):

        derivada = (
            f(x0 + h) - f(x0)
        ) / h

        st.success(
            f"Derivada aproximada = {derivada:.6f}"
        )

# =========================
# INTERPOLACIÓN
# =========================
elif metodo == "Interpolación Lineal":

    x0 = st.number_input("x0", value=1.0)
    y0 = st.number_input("y0", value=2.0)

    x1 = st.number_input("x1", value=3.0)
    y1 = st.number_input("y1", value=6.0)

    x = st.number_input("Valor a interpolar", value=2.0)

    if st.button("Calcular"):

        y = y0 + (
            (y1 - y0) / (x1 - x0)
        ) * (x - x0)

        st.success(
            f"Interpolación = {y:.6f}"
        )
