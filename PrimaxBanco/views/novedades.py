import reflex as rx
from ..components.stats_cards import stats_cards_group
from .navbar import navbar
from .table import main_table
from ..backend.backend import Download


@rx.page(route="/novedades", title="Primax Banco", description="La organización es eficiencia")
def Novedades() -> rx.Component:
    return rx.vstack(
        navbar(),
        stats_cards_group(),
        rx.button(
            "Descargar CSV",
            on_click=Download.descargar_novedades_csv,
            color_scheme="blue",
        ),
        rx.center(
            main_table(),
            width="90%",
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
        width="100%",
        spacing="5",
        justify="center",
        align="center",
        #padding_x=["2.5em", "2.5em", "3em"],
        background_color="rgb(235, 235, 235)",
    )