import streamlit as st
import utils as ut
import pandas as pd
import numpy as np
import random

ut.add_logo()



st.title("Propuesta de simulación del precio de un Airbnb")
st.write("Si usted quiere calcular el precio diario óptimo de su vivienda antes de publicar el anuncio en Airbnb, responda al siguiente cuestionario!")


listings_long = pd.read_csv("assets/Listings/listings_detail.csv")
properties = listings_long["property_type"].tolist()
properties = [x for x in properties if x!= "Casa particular (Cuba)"]
properties = [x for x in properties if x!= "Pension (South Korea)"]
option = st.selectbox("¿Qué tipo vivienda es?",
    set(properties)
    )

neigh = listings_long["neighbourhood"].tolist()
neigh = [x for x in neigh if str(x) != 'nan']
option = st.selectbox("¿En qué barrio de Madrid se encuentra?",
    set(neigh)
    )

option = st.selectbox("¿Es usted superhost en Airbnb?",
    ("Sí", "No")
    )

option = st.selectbox("¿Cómo son las habitaciones?",
    set(listings_long["room_type"].tolist())
    )

option = st.selectbox("¿De cuántos baños dispone? Se cuenta un aseo como 0.5",
    set(np.arange(1,10.5,0.5))
    )

option = st.selectbox("¿De cuántos dormitorios dispone?",
    set(np.arange(1,10.5,1))
    )

option = st.selectbox("¿Cuántos servicios ofrece la casa?",
    ("1" , "2", "3", "Más de 3")
    )

calculate = st.button("Calcular el precio diario de mi alquiler", type="primary")
if calculate:
    numero_aleatorio = random.randint(60, 200)
    numero_aleatorio = str(numero_aleatorio) + "$"
    st.metric("Precio", numero_aleatorio)
    st.write("Nótese que esta predicción es aleatoria y solo sirve como propuesta visual de uso del modelo que hemos entrenado en el notebook.")
