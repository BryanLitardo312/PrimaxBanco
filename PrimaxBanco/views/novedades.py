import reflex as rx

from PrimaxBanco.components.sidebar import sidebar_bottom_profile
from PrimaxBanco.views.data import area_chart_novedades, area_chart_novedades_casos, line_chart_novedades, line_chart_novedades_casos
from ..components.stats_cards_novedades import stats_cards_group, stats_cards_group_mobile
from .navbar import navbar,navbar_mobile
#from .table_novedades import main_table
from ..backend.backend import Download, Graphics, State
from ..components.table_actions import comandos
from ..components.table_novedades import main_table

@rx.page(route="/novedades", title="Novedades | Primax", description="La organización es eficiencia", on_load=State.verificar_sesion)
def Novedades() -> rx.Component:
    return rx.hstack(
        rx.box(
            sidebar_bottom_profile(),
        ),
        rx.vstack(
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
            rx.box(height="0.5em"),
            rx.hstack(
                rx.switch(
                    on_change=Graphics.set_novedades,
                ),
                rx.badge(
                    rx.cond(
                        Graphics.value_novedades,
                        "Novedades en USD",
                        "Novedades en # Casos"
                    ),
                    style={"fontWeight": "medium", "fontSize": "0.8em"},
                ),
            ),
            rx.cond(
                Graphics.value_novedades,
                area_chart_novedades(),
                area_chart_novedades_casos(),
            ),
            rx.box(height="0.2em"),
            comandos(),
            rx.center(
                main_table(),
                width="85%",
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
            spacing="3",
            justify="center",
            align="center",
            #padding_x=["2.5em", "2.5em", "3em"],
            background_color="rgb(245, 245, 245)",
            #background_color="#edebeb",
        ),
        background_color="white",

    )