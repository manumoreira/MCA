
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import seaborn as sns

# Configuración de la página
st.set_page_config(
    page_title="Teorema del Límite Central",
    page_icon="📊",
    layout="wide"
)

# Configurar el estilo de matplotlib
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def main():
    st.title("📊 Teorema del Límite Central: Dos Perspectivas")
    st.markdown("---")
    
    # Crear pestañas
    tab1, tab2, tab3 = st.tabs([
        "🎲 Método 1: Enfoque de Taleb (Suma de Distribuciones)",
        "📈 Método 2: Muestreo Real (Medias Muestrales)", 
        "🤔 Comparación y Explicación"
    ])
    
    with tab1:
        taleb_method()
    
    with tab2:
        sampling_method()
    
    with tab3:
        comparison_explanation()

def taleb_method():
    st.header("🎲 Método 1: Enfoque de Taleb (Suma de Distribuciones)")
    
    st.markdown("""
    **¿Qué estamos haciendo aquí?**
    Comenzamos con una distribución uniforme (plana, probabilidad igual en todas partes). 
    Cada vez que sumamos otra distribución uniforme a sí misma, el resultado se vuelve más "acampanado".
    """)
    
    # Controles
    col1, col2 = st.columns([1, 2])
    
    with col1:
        n_sumas = st.slider(
            "Número de sumas de la distribución uniforme:",
            min_value=1,
            max_value=10,
            value=1,
            key="taleb_slider"
        )
        
        st.markdown(f"**Actualmente mostrando:** Suma de {n_sumas} distribución(es) uniforme(s)")
    
    with col2:
        # Generar y mostrar la distribución
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if n_sumas == 1:
            # Distribución uniforme simple
            x = np.linspace(1, 10, 100)
            y = np.ones_like(x) * 0.111  # 1/9 para distribución uniforme(1,10)
            ax.plot(x, y, linewidth=3, label='Distribución Uniforme')
            ax.fill_between(x, y, alpha=0.3)
        else:
            # Simular suma de distribuciones uniformes
            n_samples = 10000
            sumas = np.zeros(n_samples)
            
            for _ in range(n_sumas):
                sumas += np.random.uniform(1, 10, n_samples)
            
            # Crear histograma
            ax.hist(sumas, bins=50, density=True, alpha=0.7, 
                   label=f'Suma de {n_sumas} Uniformes', edgecolor='black')
            
            # Superponer distribución normal teórica
            media_teorica = n_sumas * 5.5
            var_teorica = n_sumas * (81/12)  # varianza de uniforme(1,10)
            std_teorica = np.sqrt(var_teorica)
            
            x_normal = np.linspace(sumas.min(), sumas.max(), 100)
            y_normal = stats.norm.pdf(x_normal, media_teorica, std_teorica)
            ax.plot(x_normal, y_normal, 'r--', linewidth=2, 
                   label='Distribución Normal Teórica')
        
        ax.set_xlabel('Valor')
        ax.set_ylabel('Densidad de Probabilidad')
        ax.set_title(f'Suma de {n_sumas} Distribución(es) Uniforme(s)')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        st.pyplot(fig)
    
    # Explicación
    st.info("""
    **💡 Observación clave:** Nota cómo la distribución se vuelve más "normal" (acampanada) 
    a medida que sumas más distribuciones uniformes. Esto demuestra el principio matemático 
    subyacente: cuando sumas variables aleatorias independientes, el resultado tiende hacia 
    una distribución normal.
    """)

def sampling_method():
    st.header("📈 Método 2: Muestreo Real (Medias Muestrales)")
    
    st.markdown("""
    **¿Qué estamos haciendo aquí?**
    Tomamos repetidamente muestras de nuestra población uniforme y calculamos sus medias. 
    Aunque las muestras individuales varían, ¡la **distribución de estas medias muestrales** 
    se vuelve normal!
    """)
    
    # Controles
    col1, col2 = st.columns(2)
    
    with col1:
        tamaño_muestra = st.selectbox(
            "Tamaño de cada muestra:",
            options=[2, 5, 10, 20, 50],
            index=2
        )
        
        n_muestras = st.slider(
            "Número de muestras a tomar:",
            min_value=50,
            max_value=1000,
            value=200,
            step=50
        )
    
    with col2:
        if st.button("🎯 Tomar Muestras", type="primary"):
            # Generar muestras
            medias_muestrales = []
            
            for _ in range(n_muestras):
                muestra = np.random.uniform(1, 10, tamaño_muestra)
                medias_muestrales.append(np.mean(muestra))
            
            # Guardar en session state
            st.session_state.medias_muestrales = medias_muestrales
            st.session_state.tamaño_muestra = tamaño_muestra
            st.session_state.n_muestras = n_muestras
    
    # Mostrar resultados si existen
    if 'medias_muestrales' in st.session_state:
        medias = st.session_state.medias_muestrales
        
        # Crear gráficos lado a lado
        col1, col2 = st.columns(2)
        
        with col1:
            # Población original
            fig1, ax1 = plt.subplots(figsize=(8, 6))
            x_uniform = np.linspace(1, 10, 100)
            y_uniform = np.ones_like(x_uniform) * 0.111
            ax1.plot(x_uniform, y_uniform, linewidth=3, color='red')
            ax1.fill_between(x_uniform, y_uniform, alpha=0.3, color='red')
            ax1.set_xlabel('Valor')
            ax1.set_ylabel('Densidad de Probabilidad')
            ax1.set_title('Población Original (Uniforme)')
            ax1.grid(True, alpha=0.3)
            ax1.set_ylim(0, 0.15)
            st.pyplot(fig1)
        
        with col2:
            # Distribución de medias muestrales
            fig2, ax2 = plt.subplots(figsize=(8, 6))
            ax2.hist(medias, bins=30, density=True, alpha=0.7, 
                    color='teal', edgecolor='black')
            
            # Superponer distribución normal teórica
            media_poblacion = 5.5
            error_estandar_teorico = np.sqrt(81/12) / np.sqrt(st.session_state.tamaño_muestra)
            
            x_normal = np.linspace(min(medias), max(medias), 100)
            y_normal = stats.norm.pdf(x_normal, media_poblacion, error_estandar_teorico)
            ax2.plot(x_normal, y_normal, 'r--', linewidth=2, 
                    label='Normal Teórica')
            
            ax2.set_xlabel('Media Muestral')
            ax2.set_ylabel('Densidad')
            ax2.set_title('Distribución de Medias Muestrales')
            ax2.legend()
            ax2.grid(True, alpha=0.3)
            st.pyplot(fig2)
        
        # Estadísticas
        st.subheader("📊 Estadísticas")
        
        col1, col2, col3, col4 = st.columns(4)
        
        media_poblacion = 5.5
        promedio_medias = np.mean(medias)
        error_estandar_teorico = np.sqrt(81/12) / np.sqrt(st.session_state.tamaño_muestra)
        error_estandar_real = np.std(medias)
        
        with col1:
            st.metric("Media Poblacional", f"{media_poblacion:.2f}")
        
        with col2:
            st.metric("Promedio de Medias Muestrales", f"{promedio_medias:.3f}")
        
        with col3:
            st.metric("Error Estándar Teórico", f"{error_estandar_teorico:.3f}")
        
        with col4:
            st.metric("Error Estándar Real", f"{error_estandar_real:.3f}")
        
        # Explicación de resultados
        st.success(f"""
        **🎯 ¡Excelente!** Con {st.session_state.n_muestras} muestras de tamaño {st.session_state.tamaño_muestra}:
        
        - El promedio de las medias muestrales ({promedio_medias:.3f}) está muy cerca de la media poblacional (5.5)
        - El error estándar real ({error_estandar_real:.3f}) coincide con el teórico ({error_estandar_teorico:.3f})
        - La distribución de medias muestrales es aproximadamente normal, ¡aunque la población es uniforme!
        """)

def comparison_explanation():
    st.header("🤔 ¿Cómo se relacionan estos métodos?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎲 Enfoque de Taleb")
        st.markdown("""
        **¿Qué muestra?**
        - El principio matemático fundamental
        - Cuando sumas variables aleatorias independientes
        - El resultado tiende hacia distribución normal
        - Es una demostración teórica elegante
        
        **Fortalezas:**
        - Visualmente impactante
        - Muestra el concepto matemático puro
        - Fácil de entender intuitivamente
        """)
    
    with col2:
        st.subheader("📈 Muestreo Real")
        st.markdown("""
        **¿Qué muestra?**
        - El Teorema del Límite Central en la práctica
        - Cómo funciona con datos reales
        - Por qué las medias muestrales son confiables
        - La base de la inferencia estadística
        
        **Fortalezas:**
        - Aplicación práctica directa
        - Relevante para investigación
        - Muestra la variabilidad real
        """)
    
    st.markdown("---")
    
    st.subheader("🔗 La Conexión Clave")
    
    st.info("""
    **¿Cómo se conectan?**
    
    Una media muestral es esencialmente: **(X₁ + X₂ + ... + Xₙ) ÷ n**
    
    - La parte de **suma** (X₁ + X₂ + ... + Xₙ) sigue el principio de Taleb
    - **Dividir por n** solo cambia la escala, no la forma de la distribución
    - Por eso ambos métodos muestran normalidad
    
    **En términos simples:**
    - Taleb muestra el "por qué" matemático
    - El muestreo real muestra el "cómo" práctico
    - Ambos son la misma matemática, aplicada de forma diferente
    """)
    
    st.subheader("🎯 Implicaciones para Ciencias Sociales")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **¿Por qué es importante?**
        - Podemos hacer inferencias confiables de muestras pequeñas
        - Las medias muestrales son más estables que observaciones individuales
        - Justifica el uso de pruebas estadísticas
        - Base de intervalos de confianza
        """)
    
    with col2:
        st.warning("""
        **Condiciones importantes:**
        - Muestras deben ser aleatorias
        - Observaciones independientes
        - Tamaño de muestra suficiente (n ≥ 30 como regla general)
        - Funciona sin importar la forma de la población original
        """)
    
    st.markdown("---")
    
    st.subheader("🧠 Ejercicio de Reflexión")
    
    with st.expander("💭 Preguntas para discutir con estudiantes"):
        st.markdown("""
        1. **¿Qué pasaría si tomáramos muestras de tamaño 1?** 
           - Pista: La distribución sería igual a la población original
        
        2. **¿Por qué las medias muestrales varían menos que los datos individuales?**
           - Pista: Piensa en el efecto de promediar valores extremos
        
        3. **¿Qué significa esto para las encuestas y estudios sociales?**
           - Pista: ¿Por qué podemos confiar en resultados de muestras?
        
        4. **¿Funcionaría esto con cualquier distribución poblacional?**
           - Pista: ¡Sí! Prueba cambiando la distribución original
        
        5. **¿Cuál es la diferencia práctica entre los dos enfoques?**
           - Pista: Uno es teórico, otro simula investigación real
        """)

if __name__ == "__main__":
    main()