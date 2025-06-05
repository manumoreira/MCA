import numpy as np
import scipy as sci
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly_express as px

def main():
    st.title('MCA U5 - Test de hipótesis')
    st.subheader('Esta app permite explorar el comportamiento del test de hipótesis')
    st.write('El test de hipótesis es una medida que permite evaluar la significación estadística de una diferencia numérica ')

    data_input = st.columns((2,2,2,2,2,2))
    with data_input[0]:
        mean_pob = st.number_input("Media poblacional")
    with data_input[1]:
        stdev_pob = st.number_input("Desvio poblacional")
    with data_input[2]:
        mean_sam = st.number_input("Media muestral")
    with data_input[3]:
        sample_size = st.number_input("Tamaño muestra")    
    with data_input[4]:
        alpha_val = st.selectbox("Alfa",(0.01, 0.05)) 

    if st.button("lalala"):
        z_value = (mean_sam - mean_pob) / (stdev_pob/(np.sqrt(sample_size)))
        p_value = 1 - sci.stats.norm.cdf(z_value)
        if (p_value > alpha_val):
            "No es estadísiticamente significativo"
            print("Soy z", z_value)
            print("Soy p", p_value)
            print("Soy alfa", alpha_val)
        else:
            "Esa Cabeza!"
            x_axis = np.arange(-4, 4, 0.0001) 
            print("Soy z", z_value)
            print("Soy p", p_value)
            print("Soy alfa", alpha_val)
            gaussian = sci.stats.norm.pdf(x_axis, 0, 1)
            #gaussian = pyplot.plot(x_axis, sci.stats.norm.pdf(x_axis, mean, sd)) 
            fig, ax = plt.subplots()
            ax.plot(x_axis, gaussian, label="Distribución Gaussiana")
            ax.plot(z_value, sci.stats.norm.pdf(z_value, 0, 1), 'ro')  # 'ro' means red color, circle marker
            ax.annotate(f'p-value = {p_value}', xy=(z_value, sci.stats.norm.pdf(z_value, 0, 1)),
                xytext=(p_value + 0.5, sci.stats.norm.pdf(p_value, 0, 1) + 0.000005),
                arrowprops=dict(facecolor='black', arrowstyle='->'))
            ax.set_xlim(-4, 4)
            st.pyplot(fig)


    #if st.button("Generar du+du"):

    st.text ('Creado para la cátedra Métodos Cuantitativos en Antropología 2024')

if __name__ == "__main__":
    
    main()
