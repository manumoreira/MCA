import streamlit as st
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

def calculate_stats(numbers):
    media = np.mean(numbers)
    mediana = np.median(numbers)
    return media, mediana

def plot_histogram(numbers):
    fig, ax = plt.subplots()
    ax.hist(numbers, bins=10, alpha=0.5)
    ax.set_xlabel('Valor')
    ax.set_ylabel('Frequencia')
    ax.set_title('Histograma')
    st.pyplot(fig)

def plot_bar_chart(numbers):
    fig, ax = plt.subplots()
    unique, counts = np.unique(numbers, return_counts=True)
    plt.bar(unique, counts)
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.title('Bar Chart')
    st.pyplot(fig)

def main():
    st.title('Clase 2 - Medidas de tendencia central')

    numbers_input = st.text_area("Ingrese los números separados por comas o espacios")

    numbers = []
    for num in numbers_input.split():
        try:
            numbers.append(float(num))
        except ValueError:
            pass

    if numbers:
        mean, median = calculate_stats(numbers)
        st.write(f"Mean: {mean}")
        st.write(f"Median: {median}")
        
        plot_histogram(numbers)
        plot_bar_chart(numbers)

if __name__ == "__main__":
    main()
