import numpy as np
import matplotlib.pyplot as plt

def calculate_stats(numbers):
    mean = np.mean(numbers)
    median = np.median(numbers)
    return mean, median

def plot_histogram(numbers):
    plt.hist(numbers, bins=10, alpha=0.5)
    plt.xlabel('Valor')
    plt.ylabel('Frequencia')
    plt.title('Histograma')
    plt.show()

def plot_bar_chart(numbers):
    unique, counts = np.unique(numbers, return_counts=True)
    plt.bar(unique, counts)
    plt.xlabel('Valor')
    plt.ylabel('Contar')
    plt.title('Barras')
    plt.show()

def main():
    numbers = []
    while True:
        num = input("Enter a number (or type 'done' to finish): ")
        if num.lower() == 'done':
            break
        try:
            numbers.append(float(num))
        except ValueError:
            print("Please enter a valid number.")

    if numbers:
        mean, median = calculate_stats(numbers)
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        
        plot_histogram(numbers)
        plot_bar_chart(numbers)

if __name__ == "__main__":
    main()
