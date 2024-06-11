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
        alpha_val = st.selectbox("Alfa",(0.1, 0.5)) 

    if st.button("lalala"):
        z_val = (mean_sam - mean_pob) / (stdev_pob/(np.sqrt(sample_size)))
        test_stat = 1 - (sci.stats.norm.cdf(z_val))
        if (test_stat > alpha_val):
            "No es estadísiticamente significativo"
            print(z_val)
            print(test_stat)
        else:
            "Esa Cabeza!"
            x_axis = np.arange(-3, 3, 0.001) 
            print(test_stat)
            mean = statistics.mean(x_axis) 
            sd = statistics.stdev(x_axis) 
            plt.plot(x_axis, norm.pdf(x_axis, mean, sd)) 
            plt.show() 


    #if st.button("Generar du+du"):

    st.text ('Creado para la cátedra Métodos Cuantitativos en Antropología 2024')

if __name__ == "__main__":
    
    main()
