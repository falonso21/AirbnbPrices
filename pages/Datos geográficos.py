import streamlit as st
from streamlit_folium import folium_static
import utils as ut
import plotly
import plotly.express as px
import plotly.graph_objects as go
import folium
from folium.plugins import HeatMap, FastMarkerCluster
import branca.colormap as cm
import pandas as pd
import numpy as np
import geojson
from re import sub
from decimal import Decimal

ut.add_logo()
# Carga de datos necesarios
listings_long = pd.read_csv("assets/Listings/listings_detail.csv")
listings_long["price"] = listings_long["price"].apply(lambda x: Decimal(sub(r'[^\d.]', '', x)))
listings_long["price"] = pd.to_numeric(listings_long["price"])
with open("assets/Geo/neighbourhoods.geojson") as f:
    madrid_gj = geojson.load(f)



st.title("Estudio de la distribución geográfica de los Airbnb en la ciudad de Madrid")
st.write("En esta sección haremos un estudio sobre cómo se reparten geográficamente los Airbnb's en la ciudad de Madrid. Adquiriremos una visión global de cuales son los barrios más demandados, para después estudiar características en cada uno de ellos.")

st.header("Distribución")
st.write("En primer lugar vamos a hacer una representación de las localizaciones de los Airbnb en el mapa mediante clústers. A medida que vayamos haciendo zoom podremos ir agregando disgregando clústers al nivel de granularidad que queramos.")
madrid = folium.Map([40.4167, -3.7033], zoom_start = 11.5, tiles='CartoDB dark_matter')
FastMarkerCluster(listings_long[['latitude','longitude']].values.tolist()).add_to(madrid)
folium_static(madrid)

st.write("A continuación mostramos un mapa de calor que proporciona información similar al gráfico anterior. No obstante, aquí podemos observar más rápidamente como la mayor parte de viviendas turísiticas se encuentran en el centro de Madrid como era de esperar.")
madrid = folium.Map([40.4167, -3.7033], zoom_start = 11.5, tiles='CartoDB dark_matter')
HeatMap(listings_long[['latitude','longitude']].values.tolist(),radius=8,gradient={0.2:'blue',0.4:'purple',0.6:'orange',1.0:'red'}).add_to(madrid)
folium_static(madrid)

st.write("Una vez hemos estudiado la distribución geográfica estamos en disposición de introducir alguna variable más a nuestro estudio. La que más interés presenta es el precio, pues es la variable objetivo. Veamos entonces como influye la localización en el precio de la vivienda.")

st.header("Distribución y precio")

madrid = folium.Map([40.4167, -3.7033], zoom_start = 11, tiles='CartoDB dark_matter')
# Adaptamos la escala a nuestra variable, eliminando los outliers para que tenga sentido, si no lo veríamos todo del mismo color
colormap = cm.linear.YlOrRd_04.scale(np.percentile(listings_long["price"], 20), np.percentile(listings_long["price"], 80))

for index, row in listings_long.iterrows():
    color = colormap(row["price"])
    folium.CircleMarker(
        location= [row["latitude"], row["longitude"]],
        radius = 0.5,
        color = color,
        fill = True,
        fill_color = color,
        fill_opacity = 0.7
    ).add_to(madrid)
folium_static(madrid)

st.write("Podemos observar en el mapa anterior como se distribuyen los precios, siendo los tonos blancos precios más bajos y rojos los precios más altos. En el mapa se representa la localización de todos los Airbnb disponibles (quitando outliers). Por ello, la densisdad de puntos es muy alta. Podemos observar como el centro y la zona noreste de Madrid es la zona con, a priori, más puntos rojos. Esto nos indica que en la ciudad de Madrid los barrios más ricos se distribuyen por dicha zona, siendo el sur una zona menos exclusiva.")
st.write("Agregaremos a continuación las viviendas por barrios y mostraremos el precio medio de cada barrio, para tener una visión más concreta.")
percentiles = np.percentile(listings_long['price'], [20, 40, 60, 80])  # Puedes ajustar los percentiles

# Definir tu paleta de colores personalizada basada en los percentiles
custom_colors = px.colors.sequential.Reds 

# Calcular el precio medio por clase
mean_prices = listings_long.groupby('neighbourhood_cleansed')['price'].mean().reset_index()

fig = px.choropleth(mean_prices, geojson=madrid_gj, color="price",
                    locations="neighbourhood_cleansed", featureidkey="properties.neighbourhood",
                    projection="mercator", color_continuous_scale=custom_colors, range_color=[percentiles[0], percentiles[-1]]
                   )
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
    legend =dict(title="Precio en dólares"))
st.plotly_chart(fig)

st.write("Corroboramos en este gráfico interactivo las sospechas anteriores. La zona centro y noreste de Madrid tiene precios medios ´diarios más altos que la zona sur. Esto tiene sentido pues es donde se encuentran barrios como Salamanca, históricamente conocido por su nivel económico. Un ejercicio interesante sería cruzar estos datos con datos de renta o de actividad económica.")

st.header("Distribución y reviews")
st.write("Otra información relevante que nos arrojan los datos es la puntuación de review categorizada en diferentes temáticas.")
st.markdown(" - Reviews de precisión, que evaluan que el anuncio es fiel a lo que en realidad es la vivienda.")
st.markdown(" - Reviews de limpieza, evaluan el estado y limpieza del apartamento.")
st.markdown(" - Reviews de checkin, evaluan el horario de entrada y las facilidades que se aportan.")
st.markdown(" - Reviews de comunicación, evaluan como ha sido la comunicación con el host")
st.markdown(" - Reviews de localización, evaluan la localización del apartamento con respecto a las principales atracciones turísticas.")
st.markdown(" - Reviews de calidad precio, evaluan si las prestaciones de la vivienda van acordes al precio que tiene.")

st.write("Mostremos a continuación un mapa que indique el valor medio por barrio del tipo de review seleccionada.")

reviews_dict = {"Precisión": "review_scores_accuracy", "Limpieza": "review_scores_cleanliness", "Check-in": "review_scores_checkin", "Comunicación": "review_scores_communication", "Localización": "review_scores_location", "Calidad - precio": "review_scores_value"}

option = st.selectbox("¿Qué tipo de review quieres mostrar en el mapa?",
    reviews_dict.keys()
    )

variable = "mean_" + reviews_dict.get(option)

custom_colors = px.colors.sequential.Reds 

# Calcular el precio medio por clase
review_data = listings_long.groupby('neighbourhood_cleansed')[reviews_dict.get(option)].mean().reset_index()

fig = px.choropleth(review_data, geojson=madrid_gj, color=reviews_dict.get(option),
                    locations="neighbourhood_cleansed", featureidkey="properties.neighbourhood",
                    projection="mercator", color_continuous_scale=custom_colors
                   )
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)

st.write("Navegando entre los diferentes gráficos obtenemos resultados coherentes. Como por ejemplo que las mejores reviews de localización se encuentran en el centro, o que las mejores reviews de calidad rpecio se encuentran un poco más alejadas de dicha zona central.")
