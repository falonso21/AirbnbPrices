import streamlit as st
import utils as ut

ut.add_logo()

st.title("Estudio del precio diario de los Airbnb")
st.markdown("""
Por medio de esta aplicación se pretende hacer un análisis de diferentes factores ligados al precio de los alquileres Airbnb en Madrid. Aunque gran parte del análisis se ha llevado a cabo en el
Notebook de entrenamiento del modelo, se pretende hacer demostración del conocimiento de Streamlit mediante la visualización de resultados interesantes. Estas visualizaciones atienden principalmente
a estudios geoespaciales o de textos.

Además se propone en el último de los apartados una hipotética propuesta de uso del modelo entrenado. Pues se entiende que dicho modelo tendría potencial para que un usuario, o incluso una inmobiliaria
estudiara el mercado y optimizara el precio de la vivienda antes de publicar la oferta en Airbnb.
""")
