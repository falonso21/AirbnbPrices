import streamlit as st
import utils as ut
import pandas as pd
from PIL import Image

Languages_chart = Image.open('./assets/Languages.png')
Reviews_spanish = Image.open('./assets/Reviews_spanish.png')
English_positive = Image.open('./assets/English_positive.png')
English_negative = Image.open('./assets/English_negative.png')

ut.add_logo()

st.title("¿Qué dicen las reviews?")
st.markdown("En este apartado trataremos de estudiar el contenido de las reviews y de los textos en general que proporcionan los diferentes datasets.")
st.markdown("Puesto que Airbnb es una app enfocada al turismo y usada internacionalmente, encontraremos textos en muchas lenguas diferentes. Es esto lo primero que vamos a estudiar, la frecuencia de dichas lenguas en las reviews que tenemos como muestra.")

st.image(Languages_chart, caption='Frecuencia de idiomas', width = 600)

st.markdown("Observamos resultados lógicos pues las lenguas en la que más reviews se escriben son inglés (internacionalidad) y castellano. Luego las siguen francés y portugués por proximidad a España.")

st.header("Reviews en castellano")
st.markdown("Vamos a observar ahora qué palabras mencionan las reviews escritas en castellano.")
st.image(Reviews_spanish, caption='Wordcloud de las reviews en castellano')
st.markdown("Se observa que la mayoría de reviews versan sobre la ubicación. Otras hablan sobre localizaciones específicas como Gran Vía o Plaza Mayor. Este estudio se puede afinar más haciendo estudio de sinónimos o similaridad. Pero se escapa del alcance de esta prueba.")

st.header("Reviews en inglés")
st.markdown("Vamos a estudiar también las reviews en inglés, pero por añadir algo de sustancia, vamos a tener en cuenta la positividad o negatividad del mensaje.")

col1, col2 = st.columns(2)

with col1:
   st.image(English_positive, caption='Wordcloud de las reviews positivas en inglés')

with col2:
   st.image(English_negative, caption='Wordcloud de las reviews negativas en inglés')

st.markdown("En las reviews de tono positivo se encuentran resultados esperados con frases como 'highly recommended' o 'grat location'. Sin embargo, obtenemos resultados curiosos en la nube de palabras de las reviews negaivas; si bien es cierto que encontramos frases que denotan negativdad como 'canceled reservation' o 'problem'. También encontramos muchas otras que parecen denotar positividad. Esto puede ser debido a que en una review, la queja solo sea uno de los comentarios de entre otros comentarios positivos." )