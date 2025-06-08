import reflex as rx
from reflex.components.radix.themes.base import (
    LiteralAccentColor,
)

from ..backend.backend import State


def _arrow_badge(arrow_icon: str, percentage_change: float, arrow_color: str):
    return rx.badge(
        rx.icon(
            tag=arrow_icon,
            color=rx.color(arrow_color, 9),
        ),
        rx.hstack(
            rx.text(
                f"{percentage_change}",
                size="3",
                color=rx.color(arrow_color, 9),
                weight="medium",
            ),
            rx.text(
                f"/semana",
                size="2",
                color=rx.color(arrow_color, 9),
                weight="medium",
            ),
            spacing="1",
            align="end",
        ),
        color_scheme=arrow_color,
        radius="large",
        align_items="center",
    )


def stats_card(
    stat_name: str,
    value: int,
    #prev_value: int,
    incremento: int,
    icon: str,
    icon_color: LiteralAccentColor,
    #extra_char: str = "",
) -> rx.Component:
    return rx.card(
            rx.vstack(
                rx.box(
                    rx.hstack(
                        rx.heading(
                            f"{value}",
                            size="8",
                            weight="bold",
                        ),
                        rx.spacer(),
                        rx.cond(
                            incremento > 0,
                            _arrow_badge("trending-up", incremento, "grass"),
                            _arrow_badge("trending-down", incremento, "tomato"),
                        ),
                        #spacing="6",
                        #align='center',
                        width="100%",
                        justify="between",
                    ),
                    margin_bottom="0.7em",
                    width="100%",
                ),
                rx.hstack(
                    rx.hstack(
                        rx.icon(
                            tag=icon,
                            size=22,
                            color=rx.color(icon_color, 11),
                        ),
                        rx.text(
                            stat_name,
                            size="4",
                            weight="medium",
                            color="#000000",
                        ),
                        spacing="2",
                        align="center",
                    ),
                    justify="between",
                    width="100%",
                ),
                
                rx.text(
                    "Reportadas por Estaciones de Servicio",
                    size="2",
                    color=rx.color("gray", 11),
                    #weight="bold",
                ),
                align_items="start",
                justify="between",
                width="100%",
                spacing="1",
            ),
        size="3",
        width="30%",
        border="2px solid #e0e0e0",
        box_shadow="0 4px 24px rgba(0,0,0,0.08)",
        transition="box-shadow 0.2s",
        _hover={"box_shadow": "0 8px 32px rgba(0,0,0,0.12)", "border": "1.5px solid #009639"},
        #max_width="20rem",
    )


def stats_cards_group() -> rx.Component:
    return rx.hstack(
        stats_card(
            "Novedades bancarias",
            State.load_novedades,
            State.novedades_diarias,
            "users",
            "blue",
        ),
        rx.spacer(),
        stats_card(
            "Suministros Blindado",
            State.load_suministros,
            State.novedades_diarias,
            "dollar-sign",
            "orange",
            
        ),
        rx.spacer(),
        stats_card(
            "Retrasos y Quejas",
            State.load_quejas,
            State.novedades_diarias,
            "truck",
            "ruby",
        ),
        align="center",
        justify="center",
        spacing="3",
        width="80%",
        #margin_top="2em",
        margin_bottom="3em",
        #wrap="wrap",
        #display=["none", "none", "flex"],
    )
