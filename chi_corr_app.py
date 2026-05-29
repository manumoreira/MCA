import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Configuración
st.set_page_config(page_title="Comparativa de Tests", layout="wide")
st.title("De lo Continuo a lo Categórico: Pearson, Spearman y Chi-Cuadrado")
st.markdown("Analizamos 20 individuos de una comunidad. Variables: **Edad** y **Fluidez Lingüística**.")

# --- GENERACIÓN DE DATOS (20 casos fijos por escenario para evitar saltos) ---
@st.cache_data
def generar_datos(escenario):
    np.random.seed(42) # Semilla fija para que los 20 sujetos sean siempre los mismos
    n = 20
    edad = np.round(np.linspace(18, 75, n))
    
    if escenario == "Relación Lineal Fuerte":
        fluidez = edad + np.random.normal(0, 5, n)
    elif escenario == "Sin Relación":
        fluidez = np.random.uniform(20, 90, n)
    elif escenario == "Relación Curva (No lineal)":
        # Fluidez alta en edades medias, baja en extremos
        fluidez = -0.05 * (edad - 45)**2 + 85 + np.random.normal(0, 5, n)
    elif escenario == "Con un Outlier Extremo":
        fluidez = edad + np.random.normal(0, 5, n)
        edad[0] = 20
        fluidez[0] = 95 # Un joven con fluidez atípicamente perfecta
        
    fluidez = np.clip(np.round(fluidez), 0, 100) # Limitar entre 0 y 100
    
    df = pd.DataFrame({'Sujeto': range(1, 21), 'Edad': edad, 'Fluidez': fluidez})
    
    # Transformaciones didácticas
    df['Rango_Edad'] = df['Edad'].rank()
    df['Rango_Fluidez'] = df['Fluidez'].rank()
    
    # Categorización en Terciles (Bajo, Medio, Alto)
    df['Cat_Edad'] = pd.qcut(df['Edad'], q=3, labels=['Jóvenes', 'Adultos', 'Mayores'])
    df['Cat_Fluidez'] = pd.qcut(df['Fluidez'], q=3, labels=['Básica', 'Media', 'Avanzada'])
    
    return df

# --- INTERFAZ ---
escenario = st.sidebar.selectbox(
    "Elegí el comportamiento de los 20 sujetos:",
    ("Relación Lineal Fuerte", "Relación Curva (No lineal)", "Sin Relación", "Con un Outlier Extremo")
)

df = generar_datos(escenario)

# --- PANEL SUPERIOR: DATOS Y TABLA DE CONTINGENCIA ---
st.header("1. Mirando los Datos")
col_data, col_crosstab = st.columns([1.5, 1])

with col_data:
    st.subheader("Los 20 Sujetos")
    # Mostramos la tabla formateada para que entiendan la transformación
    st.dataframe(
        df[['Sujeto', 'Edad', 'Fluidez', 'Rango_Edad', 'Rango_Fluidez', 'Cat_Edad', 'Cat_Fluidez']], 
        hide_index=True, height=250
    )

with col_crosstab:
    st.subheader("Tabla de Contingencia")
    st.markdown("Recuento de los 20 sujetos según sus categorías:")
    tabla_cont = pd.crosstab(df['Cat_Edad'], df['Cat_Fluidez'], margins=True, margins_name="Total")
    st.table(tabla_cont)

st.divider()

# --- PANEL INFERIOR: GRÁFICO Y RESULTADOS ---
st.header("2. Visualización y Tests Estadísticos")
col_plot, col_results = st.columns([1.5, 1])

with col_plot:
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df['Edad'], df['Fluidez'], color='dodgerblue', s=80, edgecolor='black', zorder=5)
    
    for i, txt in enumerate(df['Sujeto']):
        ax.annotate(txt, (df['Edad'].iloc[i]+1, df['Fluidez'].iloc[i]+1), fontsize=9, color='gray')

    # Líneas divisorias de los terciles (la grilla de Chi-cuadrado)
    q_edad = df['Edad'].quantile([0.33, 0.66]).values
    q_fluidez = df['Fluidez'].quantile([0.33, 0.66]).values
    
    ax.axvline(q_edad[0], color='red', linestyle='--', alpha=0.5)
    ax.axvline(q_edad[1], color='red', linestyle='--', alpha=0.5)
    ax.axhline(q_fluidez[0], color='red', linestyle='--', alpha=0.5)
    ax.axhline(q_fluidez[1], color='red', linestyle='--', alpha=0.5)
    
    ax.set_title("Nube de Puntos + Cuadrícula Categórica (Terciles)")
    ax.set_xlabel("Edad (Años)")
    ax.set_ylabel("Fluidez Lingüística (0-100)")
    ax.grid(True, alpha=0.2)
    st.pyplot(fig)

with col_results:
    st.subheader("Resultados de los Tests")
    
    # 1. Pearson
    r, p_pearson = stats.pearsonr(df['Edad'], df['Fluidez'])
    st.markdown(f"**1. Correlación de Pearson (Datos exactos)**")
    st.code(f"r = {r:.3f} | p-valor = {p_pearson:.4f}")
    if p_pearson < 0.05:
        st.success("Significativo (Capta la asociación lineal)")
    else:
        st.error("No Significativo (No capta asociación lineal)")
        
    # 2. Spearman
    rho, p_spearman = stats.spearmanr(df['Edad'], df['Fluidez'])
    st.markdown(f"**2. Correlación de Spearman (Por Rangos)**")
    st.code(f"rho = {rho:.3f} | p-valor = {p_spearman:.4f}")
    if p_spearman < 0.05:
        st.success("Significativo (Capta la asociación monótona)")
    else:
        st.error("No Significativo (No capta asociación monótona)")

    # 3. Chi-Cuadrado
    # Recalculamos la tabla sin los márgenes para el test
    tabla_test = pd.crosstab(df['Cat_Edad'], df['Cat_Fluidez'])
    chi2, p_chi2, dof, expected = stats.chi2_contingency(tabla_test)
    st.markdown(f"**3. Test de Chi-Cuadrado (Por Categorías 3x3)**")
    st.code(f"X² = {chi2:.3f} | p-valor = {p_chi2:.4f}")
    if p_chi2 < 0.05:
        st.success("Significativo (Capta agrupamientos en las celdas)")
    else:
        st.error("No Significativo (La muestra es chica o no hay patrón)")