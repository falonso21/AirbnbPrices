import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Airbnb_Logo_B%C3%A9lo.svg/250px-Airbnb_Logo_B%C3%A9lo.svg.png);
                background-repeat: no-repeat;
                padding-top: 35px;
                background-position: 20px 80px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def plot_stats_uni(data):
    X = ['3 años', '6 años', '10 años', '20 años']
    prob = [data["Prob 3 años"].tolist()[0], data["Prob 6 años"].tolist()[0], data["Prob 10 años"].tolist()[0],
            data["Prob 20 años"].tolist()[0]]
    conf = [data["Confianza 3 años"].tolist()[0], data["Confianza 6 años"].tolist()[0],
            data["Confianza 10 años"].tolist()[0], data["Confianza 20 años"].tolist()[0]]

    X_axis = np.arange(len(X))

    plt.bar(X_axis - 0.2, prob, 0.4, label='Probabilidad')
    plt.bar(X_axis + 0.2, conf, 0.4, label='Conf levl')

    plt.xticks(X_axis, X)
    plt.xlabel("Años")
    plt.title("Probabilidad y confidence level de obtención de sexenio")
    plt.legend()
    plt.show()


predictions = {"Nombre": ["Pedro Aguilar", "María Villar", "Paula Esteban"],
               "Departamento": ["Ciencias de la salud", "Humanidades", "Ciencias de la salud"],
               "Prob 3 años": [0.2, 0.7, 0.3],
               "Confianza 3 años": [0.6, 0.8, 0.5], "Prob 6 años": [0.5, 0.8, 0.6], "Confianza 6 años": [0.7, 0.8, 0.7],
               "Prob 10 años": [0.7, 0.9, 0.9], "Confianza 10 años": [0.8, 0.9, 0.9], "Prob 20 años": [0.8, 0.9, 0.9],
               "Confianza 20 años": [0.9, 0.9, 0.9]}
pred_sexenios = pd.DataFrame(data=predictions)
