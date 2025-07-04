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
            type_="linear",
            #stroke="#8884d8",
            #stroke="#050240",
            dot={"stroke": "#080808", "fill": "#cccccc"},
            active_dot={"stroke": "#080808", "fill": "#cccccc"},
            stroke="#080808",
            stroke_width=2,
            name="Total reportado",
        ),
        rx.recharts.cartesian_grid(
            stroke="#cccccc",           # Color de la cuadrícula
            stroke_dasharray="3 3",     # Patrón de guiones
            fill="#f9f9f9",             # Color de fondo de la cuadrícula
            fill_opacity=0.3,           # Opacidad del fondo
        ),
        rx.recharts.x_axis(
            data_key="FECHA",
            hide=True,
            #tick={
            #"angle": -90,
            #"text_anchor": "end",
            #"dy": 50
            #},
            #height=50,
            #label={"value": "Fecha", "position": "bottom", "fill": "#555555"},
        ),
        rx.recharts.graphing_tooltip(
            content_style={
                "backgroundColor": rx.color("accent", 4),
                "borderRadius": "4px",
                "padding": "8px",
            },
        ),
        rx.recharts.y_axis(
            type_="number",
            stroke=rx.color("gray", 12),
            axis_line=False,
            unit="$",
            mirror=False,
        ),
        data=Graphics.novedades_acumuladas,
        width="80%",
        height=300,
    )

def bar_tres_barras_novedades():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="Acumulado",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(
            data_key="ESTACION",
            hide=True,
        ),
        rx.recharts.graphing_tooltip(
            content_style={
                "backgroundColor": rx.color("accent", 4),
                "borderRadius": "4px",
                "padding": "8px",
            },
        ),
        rx.recharts.y_axis(
            type_="number",
            stroke=rx.color("gray", 12),
            axis_line=False,
            unit="$",
            mirror=False,
        ),
        data=Graphics.novedades_acumuladas_estacion,  # data debe ser una lista de diccionarios con las claves "uv", "pv" y "amt"
        width="80%",
        height=200,
    )

@rx.page(route="/data",title="Data | Primax",description="Data en Primax Banco")
def data() -> rx.Component:
        return rx.box(
            rx.vstack(
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
                rx.heading('Evolución mensual'),
                #rx.box(height="1em"),
                line_chart_novedades(),
                #rx.box(height="1em"),
                bar_tres_barras_novedades(),
                rx.box(height="2em"),
                spacing="2",
                align_items="center",
            ),
            rx.box(
                rx.text(
                    "Primax Corporativo - Todos los derechos reservados",
                    size="2",
                    color="gray",
                    text_align="center",
                ),
                width="100%",
                padding_y="4em",
            ),
            width="100vw",
            height="100vh",
        ),