import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

def calculate_stats(numbers):
    mean = np.mean(numbers)
    median = np.median(numbers)
    return mean, median

def main():
    st.title('MCA Clase 2 - Medidas de tendencia Central')

    numbers_input = st.text_area("ingrese números separados por espacio")

    numbers = []
    for num in numbers_input.split():
        try:
            numbers.append(float(num))
        except ValueError:
            pass

    if numbers:
        mean, median = calculate_stats(numbers)
        st.write(f"Media: {mean}")
        st.write(f"Mediana: {median}")

        st.write("### Histograma")
        hist_data = pd.DataFrame({'Numeros': numbers})
        chart = alt.Chart(hist_data).mark_bar().encode(
            x=alt.X('Numeros', bin=True),
            y='count()'
        ).properties(
            width=600,
            height=300
        )
        st.altair_chart(chart)

        st.write("### Barras")
        unique, counts = np.unique(numbers, return_counts=True)
        data = pd.DataFrame({'Value': unique, 'Count': counts})
        st.bar_chart(data.set_index('Value'))

if __name__ == "__main__":
    main()
