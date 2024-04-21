import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd

def calculate_stats(numbers):
    mean = np.round(np.mean(numbers),3)
    median = np.median(numbers)
    std = np.round(np.std(numbers, ddof=1),3)
    variance = np.round(np.var(numbers),3)
    minim = np.min(numbers)
    q1 = np.quantile(numbers, 0.25)
    q3 = np.quantile(numbers, 0.70)
    maxim = np.max(numbers)
    intq= q3 - q1

    return mean, median, std, q1, q3, minim, maxim, variance, intq

def parse_input(numbers_input):
    # Split input by comma, space, or newline
    numbers = []
    for num in numbers_input.replace('\n', ',').split(','):
        # Split by space as well
        for num_split in num.strip().split():
            try:
                numbers.append(float(num_split.strip()))
            except ValueError:
                pass
    return numbers

def main():
    st.title('MCA U2 - Graficación, frecuencias, medidas de tendencia central y dispersión')
    st.subheader('Esta app calcula media, mediana, grafica histograma y gráfico de barras')

    numbers_input = st.text_area("Ingrese números separados por coma, espacio o enter")

    if st.button("Calcular"):
        numbers = parse_input(numbers_input)

        if numbers:
            mean, median, std, q1, q3, minim, maxim, variance, intq = calculate_stats(numbers)
            st.write(f"Media: {mean}")
            st.write(f"Varianza: {variance}")
            st.write(f"Desvio Estandar Muestral: {std}")
            st.write("#### Cinco números de resumen")
            st.write(f"Mínimo: {minim}")
            st.write(f"1 Cuartil: {q1}")
            st.write(f"Mediana: {median}")
            st.write(f"3 Cuartil: {q3}")
            st.write(f"Máximo: {maxim}")
            st.write(f"Intervalo intercuartil: {intq}")

            st.write("### Histograma")
            hist_data = pd.DataFrame({'Numeros': numbers})
            fig = px.histogram(hist_data, x='Numeros', nbins=len(set(numbers)))
            fig.add_vline(x=mean, line_dash="dash", line_color="red", name="Media")
            fig.add_vline(x=median, line_dash="dash", line_color="green", name="Mediana")
            st.plotly_chart(fig)

            st.write("### Box Plot")
            box_data = pd.DataFrame({'Numeros': numbers})
            fig = px.box(box_data, y='Numeros')
            st.plotly_chart(fig)

    st.text ('Creado para la cátedra Métodos Cuantitativos en Antropología 2024')

if __name__ == "__main__":
    main()
