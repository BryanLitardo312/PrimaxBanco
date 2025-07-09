import reflex as rx
from ..components.stats_cards_devoluciones import stats_cards_group, stats_cards_group_mobile
from .navbar import navbar,navbar_mobile
from ..components.table_devoluciones import main_table
from ..backend.backend import Download, State
from ..components.table_actions import comandos_devoluciones

@rx.page(route="/devoluciones", title="Devoluciones | Primax", description="La organización es eficiencia",on_load=State.verificar_sesion)
def Devoluciones() -> rx.Component:
    return rx.vstack(
        #navbar(),
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
        rx.tablet_and_desktop(
            rx.center(
                stats_cards_group(),
                width="100%",
            ),
            width="100%",
        ),
        rx.mobile_only(
            rx.center(
                stats_cards_group_mobile(),
                width="100%",
            ),
            width="100%",
        ),
        #stats_cards_group(),
        rx.box(height="0.5em"),
        rx.heading(
            "Devoluciones bancarias",
            size="7",
            color="black",
            text_align="center",
        ),
        rx.box(height="1em"),
        comandos_devoluciones(),
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
        background_color="rgb(245, 245, 245)",
    )