# Simulando datos
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly_express as px

def main():
    st.title('MCA U4 - Teorema central del límite')
    st.subheader('Esta app permite una aproximación conceptual al TCL')
    st.write('Al sumarse repetidas veces muchas distribuciones van a tender a una distribución normal')

    st.write('Esta app está inspirada en esta pseudo-demostración intuitiva de Nassim Taleb https://youtu.be/bfM9efdStN8?si=TCVAD1uxm8rjzCep')

    st.write ('Primero generamos una distribución uniforme de números entre 0 y 10 que llamaremo du (Distribución Uniforme)')

    if st.button("Generar du"):

        ## De distribuciones uniformes a distribuciones normales
        # Distribucion uniforme
        st.write("### Histograma Distribución Uniforme")
        a = np.random.uniform(0, 10, 10000)
        fig1 = px.histogram(a)
        st.plotly_chart(fig1, use_container_width=True)
        
        
        #plt.figure(figsize=(10, 5))
        #plt.subplot(1, 2, 1)
        #unifo = sns.histplot(a)
        #plt.title('Distribución Uniforme')

    st.text ('Luego sumaremos esa distribución a si misma du + du')
    
    if st.button("Generar du+du"):

        for i in range(0,10000):
            b = np.random.uniform(0, 10, 10000)
            b = b + np.random.uniform(0, 10, 10000)

        st.write("### Histograma du + du")
        fig2 = px.histogram(b)
        st.plotly_chart(fig2, use_container_width=True)
        
    st.text ('Por ultimo haremos varias sumas de du (du*6)')
    
    if st.button("Generar du*6"):

        for i in range(0,10000):
            b = np.random.uniform(0, 10, 10000)
            b = b + np.random.uniform(0, 10, 10000)
            b = b + np.random.uniform(0, 10, 10000)
            b = b + np.random.uniform(0, 10, 10000)
            b = b + np.random.uniform(0, 10, 10000)
            b = b + np.random.uniform(0, 10, 10000)


        st.write("### Histograma du*6")
        fig3 = px.histogram(b)
        st.plotly_chart(fig3, use_container_width=True)

    st.text ('Creado para la cátedra Métodos Cuantitativos en Antropología 2024')

if __name__ == "__main__":
    
    main()
