import streamlit as st
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

def calculate_stats(numbers):
    mean = np.mean(numbers)
    median = np.median(numbers)
    return mean, median

def plot_histogram(numbers):
    plt.hist(numbers, bins=10, alpha=0.5)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    st.pyplot()

def plot_bar_chart(numbers):
    unique, counts = np.unique(numbers, return_counts=True)
    plt.bar(unique, counts)
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.title('Bar Chart')
    st.pyplot()

def main():
    st.title('Simple Stats Tool')

    numbers_input = st.text_area("Enter numbers separated by spaces or commas")

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
