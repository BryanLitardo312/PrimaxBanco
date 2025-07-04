import reflex as rx
from ..backend.backend import State,Graphics
from datetime import datetime
from .navbar import navbar, navbar_mobile
import plotly.express as px

color2 = "rgb(130,130,130)"



#def line_chart_novedades_plotly():
    #return rx.center(
        #rx.plotly(data=Graphics.fig_line),
        #width="80%",
        #height="300px",
    #)

def line_chart_novedades():
    return rx.recharts.line_chart(
        rx.recharts.line(
            data_key="VALOR",
            stroke="#8884d8",
        ),
        rx.recharts.cartesian_grid(
            stroke="#cccccc",           # Color de la cuadrícula
            stroke_dasharray="3 3",     # Patrón de guiones
            fill="#f9f9f9",             # Color de fondo de la cuadrícula
            fill_opacity=0.3,           # Opacidad del fondo
        ),
        rx.recharts.x_axis(
            data_key="FECHA",
            label={"value": "Fecha", "position": "bottom", "fill": "#555555"},
        ),
        rx.recharts.y_axis(label={"value": "Valor", "angle": -90, "position": "left", "fill": "#555555"},),
        data=Graphics.novedades_acumuladas,
        width="80%",
        height=300,
    )

def bar_tres_barras():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="ACUMULADO",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(data_key="ESTACION",
            tick={
            "angle": -90,
            "text_anchor": "start",
            #"dy": 10
            }
        ),
        rx.recharts.y_axis(),
        data=Graphics.novedades_acumuladas_estacion,  # data debe ser una lista de diccionarios con las claves "uv", "pv" y "amt"
        width="80%",
        height=250,
    )

@rx.page(route="/data",title="Data | Primax",description="Data en Primax Banco")
def data() -> rx.Component:
    return rx.vstack(
        rx.tablet_and_desktop(
            rx.center(
                navbar(),
                width="100%",
            ),
            width="100%",
        ),
        rx.mobile_only(
            rx.center(
                navbar_mobile(),
                width="100%",
            ),
            width="100%",
        ),
        rx.box(height="2em"),
        line_chart_novedades(),
        bar_tres_barras(),
        align_items="center",
    )