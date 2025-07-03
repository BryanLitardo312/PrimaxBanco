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
        rx.recharts.x_axis(data_key="FECHA"),
        rx.recharts.y_axis(),
        data=Graphics.novedades_acumuladas,
        width="80%",
        height=300,
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
        rx.box(height="10em"),
        line_chart_novedades(),
        align_items="center",
    )