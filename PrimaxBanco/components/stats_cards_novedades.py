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
            align="center",
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
    texto: str,
    #extra_char: str = "",
) -> rx.Component:
    return rx.card(
            rx.vstack(
                rx.box(
                    rx.hstack(
                        rx.heading(
                            f"{value}",
                            #size="8",
                            style={"font_size": "2.5em"},
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
                    rx.icon(
                            tag=icon,
                            size=32,
                            color=rx.color(icon_color, 11),
                    ),
                    rx.vstack(
                        rx.text(
                            stat_name,
                            size="3",
                            weight="medium",
                            color="#000000",
                        ),
                        rx.text(
                            texto,
                            size="2",
                            color=rx.color("gray", 11),
                            #weight="bold",
                        ),
                        spacing="0",
                        align="start",
                    ),
                    justify="start",
                    align="center",
                    width="100%",
                ),
                
                align_items="start",
                justify="between",
                width="100%",
                spacing="2",
            ),
        padding="1.5em",
        size="3",
        #width="30%",
        width=["100%", "100%", "30%"],
        border="2px solid #0a0a0a",
        box_shadow="0 4px 24px rgba(0,0,0,0.08)",
        transition="box-shadow 0.2s",
        _hover={"box_shadow": "0 8px 32px rgba(0,0,0,0.12)", "border": "3px solid #009639"},
        #max_width="20rem",
    )

def stats_card2(
    stat_name: str,
    value: int,
    #prev_value: int,
    incremento: int,
    icon: str,
    icon_color: LiteralAccentColor,
    texto: str,
    #extra_char: str = "",
) -> rx.Component:
    return rx.card(
            rx.vstack(
                rx.box(
                    rx.hstack(
                        rx.heading(
                            f"{value}",
                            #size="8",
                            style={"font_size": "2.5em"},
                            weight="bold",
                        ),
                        rx.spacer(),
                        rx.cond(
                            incremento < 0,
                            rx.badge(
                                rx.icon(
                                    tag="check",
                                    color=rx.color("grass", 9),
                                    size=15,
                                ),
                                rx.text("Al día", size="2", color=rx.color("grass", 9), weight="medium"),
                                color_scheme="grass",
                            ),
                            rx.badge(
                                rx.icon(
                                    tag="ban",
                                    color=rx.color("tomato", 9),
                                    size=15,
                                ),
                                rx.text("Atrasado", size="2", color=rx.color("tomato", 9), weight="medium"),
                                color_scheme="tomato",
                            ),
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
                    rx.icon(
                            tag=icon,
                            size=32,
                            color=rx.color(icon_color, 11),
                    ),
                    rx.vstack(
                        rx.text(
                            stat_name,
                            size="3",
                            weight="medium",
                            color="#000000",
                        ),
                        rx.text(
                            texto,
                            size="2",
                            color=rx.color("gray", 11),
                            weight="light",
                        ),
                        spacing="0",
                        align="start",
                    ),
                    justify="start",
                    align="center",
                    width="100%",
                ),
                align_items="start",
                justify="between",
                width="100%",
                spacing="2",
            ),
        padding_y="1.5em",
        size="3",
        #width="30%",
        width=["100%", "100%", "30%"],
        border="2px solid #0a0a0a",
        box_shadow="0 4px 24px rgba(0,0,0,0.08)",
        transition="box-shadow 0.2s",
        _hover={"box_shadow": "0 8px 32px rgba(0,0,0,0.12)", "border": "3px solid #009639"},
        #max_width="20rem",
    )


def stats_cards_group() -> rx.Component:
    return rx.hstack(
        stats_card(
            "Novedades bancarias",
            State.load_novedades,
            State.novedades_diarias,
            "landmark",
            "blue",
            "Eventos acumulados",
        ),
        rx.spacer(),
        stats_card2(
            "Procesos pendientes",
            State.load_novedades_pendientes,
            State.novedades_diarias,
            "notebook-pen",
            "orange",
            "Eventos acumulados",
            
        ),
        rx.spacer(),
        stats_card(
            "Retrasos y Quejas",
            State.load_quejas,
            State.quejas_diarias,
            "calendar-x-2",
            "ruby",
            "Eventos acumulados",
        ),
        align="center",
        justify="center",
        spacing="3",
        width="80%",
        margin_top="1em",
        margin_bottom="3em",
        #wrap="wrap",
    )

def stats_cards_group_mobile() -> rx.Component:
    return rx.vstack(
        stats_card(
            "Novedades bancarias",
            State.load_novedades,
            State.novedades_diarias,
            "landmark",
            "blue",
            "Eventos acumulados",
        ),
        #rx.spacer(),
        stats_card2(
            "Procesos pendientes",
            State.load_novedades_pendientes,
            State.novedades_diarias,
            "notebook-pen",
            "orange",
            "Eventos acumulados",
            
        ),
        #rx.spacer(),
        stats_card(
            "Retrasos y Quejas",
            State.load_quejas,
            State.quejas_diarias,
            "calendar-x-2",
            "ruby",
            "Eventos acumulados",
        ),
        align="center",
        justify="center",
        spacing="3",
        width="80%",
        margin_top="1em",
        margin_bottom="3em",
        #display=["flex", "none", "none"],
        #wrap="wrap",
    )
