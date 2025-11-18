# Ejecutar con: streamlit run dashboard/app.py
import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Dashboard Premier League Insights")
    st.write("El set de datos contiene una amplia informacion acerca del rendimiento de los jugadores de la Premier League en diferentes partidos y equipos. Todos estos datos nos pueden revelar patrones en el comportamiento de los futbolistas.")

    st.write("## Rendimiento a nivel club vs nacional")
    df = pd.read_csv(r'src\data\processed\premier_clean.csv')

    seleccion_equipo = st.selectbox("Seleccione un equipo", df["Team"].unique())
    filtro_equipo = df[df["Team"] == seleccion_equipo]
    goleadores_club = (
        filtro_equipo
        .groupby("Player")["Goals"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )
    fig = px.bar(goleadores_club, x="Player", y="Goals", title=f'Top 5 goleadores maximos en {seleccion_equipo}')
    st.plotly_chart(fig)


    nombre_goleador_club = goleadores_club["Player"].iloc[0]
    promedio_minutos = filtro_equipo[filtro_equipo["Player"] == nombre_goleador_club]["Minutes"].mean().round(1)
    edad =  filtro_equipo[filtro_equipo["Player"] == nombre_goleador_club]["Age"].iloc[0]

    st.write(f'El maximo goleador de la temporada del {seleccion_equipo} es {nombre_goleador_club}, quien con una edad de {edad} años tiene un promedio de {promedio_minutos} minutos en el campo y demuestra ser uno de los favoritos del equipo tecnico.')

    pais_de_goleador = df[df["Player"] == nombre_goleador_club]["Nation"].iloc[0]
    goleadores_nacion = (
        df[df["Nation"] == pais_de_goleador]
        .groupby("Player")["Goals"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )
    fig = px.bar(goleadores_nacion, x="Player", y="Goals", title=f'Top 5 goleadores maximos en {pais_de_goleador}', color_discrete_sequence=["white"])
    st.plotly_chart(fig)

    nombre_goleador_nacion = goleadores_nacion["Player"].iloc[0]

    if nombre_goleador_club == nombre_goleador_nacion:
        st.write(f"A nivel nacional tambien demuestra ser el maximo goleador, demostrando que el {seleccion_equipo} a hecho una excelente decision al seleccionarlo como uno de sus jugadores")
    else:
        st.write(f"Sin embargo, a nivel nacional, el club pudo haber elegido a mejores jugadores, como es el caso de {nombre_goleador_nacion}, quien suma una mayor cantidad de goles.")



    st.write("## Son necesarias las faltas para marcar goles?")

    df["Tarjetas totales"] = df["Yellow Cards"] + df["Red Cards"]

    fig1 = px.scatter(
        df,
        x="Tarjetas totales",
        y="Goals",
        title="Tarjetas vs Goles"
    )

    st.plotly_chart(fig1)

    st.write("Los datos nos demuestran que, de hecho, cometer faltas a lo largo del partido reduce considerablemente la cantidad goles que marcan los jugadores.")


    fig2 = px.scatter(
        df,
        x="Tarjetas totales",
        y="Pass Completion %",
        title="Tarjetas vs Pases Completados"
    )

    st.plotly_chart(fig2)

    st.write("Al graficar la relacion entre los pases completados y las tarjetas recibidas, vemos como tampoco se ve justificada esta accion, ya que no se ve un patron claro. Esto se puede deber a que las faltas no se suelen cometer en acciones ofensivas, si no mas bien, en las defensivas. Sin embargo, se puede ver como claramente no es un factor que favorezcan en el avance del juego.")


if __name__ == "__main__":
    main()