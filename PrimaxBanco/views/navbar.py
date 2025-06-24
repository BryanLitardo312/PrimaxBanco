import reflex as rx
from ..backend.backend import State

color_bg = "rgb(3, 3, 45)"

"""def navbar():
    return rx.flex(
        rx.badge(
            rx.icon(tag="table-2", size=28),
            rx.heading("Customer Data App", size="6"),
            color_scheme="green",
            radius="large",
            align="center",
            variant="surface",
            padding="0.65rem",
        ),
        rx.spacer(),
        rx.hstack(
            rx.logo(),
            rx.color_mode.button(),
            align="center",
            spacing="3",
        ),
        spacing="2",
        flex_direction=["column", "column", "row"],
        align="center",
        width="100%",
        top="0px",
        padding_top="2em",
    )"""


def navbar():
    return rx.box(
        rx.hstack(
            # Logo a la izquierda
            rx.box(
                rx.image(
                src="/primax_logo.png",
                width="auto",
                height="40px",
                alt="Logo Primax",
                ),
                background_color="white",
                border_radius="2em",
                #width="100%",
            ),
            rx.spacer(),  # Empuja los botones a la derecha
            # Botones a la derecha
            rx.hstack(
                rx.link(
                    rx.text(
                        "Inicio",
                        size="4",
                        style={
                            "color": "white",
                            "fontWeight": "medium",
                            "transition": "all 0.2s ease-in-out",
                            "_hover": {
                                "transform": "scale(1.20)",
                            },
                        },
                    ),
                    href="/novedades",
                ),
                rx.link(
                    rx.text(
                        "Novedades",
                        size="4",
                        style={
                            "color": "white",
                            "fontWeight": "medium",
                            "transition": "all 0.2s ease-in-out",
                            "_hover": {
                                "transform": "scale(1.20)",
                            },
                        },
                    ),
                    href="/novedades",
                ),
                rx.link(
                    rx.text(
                        "Suministros",
                        size="4",
                        style={
                            "color": "white",
                            "fontWeight": "medium",
                            "transition": "all 0.2s ease-in-out",
                            "_hover": {
                                "transform": "scale(1.20)",
                            },
                        },
                    ),
                    href="/novedades",
                ),
                rx.link(
                    rx.text(
                        "Devoluciones",
                        size="4",
                        style={
                            "color": "white",
                            "fontWeight": "medium",
                            "transition": "all 0.2s ease-in-out",
                            "_hover": {
                                "transform": "scale(1.20)",
                            },
                        },
                    ),
                    href="/novedades",
                ),
                spacing="9",
                justify="between",
                width="60%",
            ),
            rx.spacer(),
            rx.box(
                rx.text(State.email),
                style={"fontWeight": "bold", "color": "grey"},
                #height="100%",
                display="flex",
                align_items="center",
                background_color="white",
                border_radius="2em",
                padding_x="2em",
                height="40px",
            ),
            rx.box(
                rx.button(
                    rx.icon(tag="log-out", size=20),
                    color_scheme="red",
                    variant="ghost",
                    size="4",
                    width="100%",
                    on_click=State.logout,
                ),
                style={"fontWeight": "bold", "color": "grey"},
                #height="100%",
                display="flex",
                align_items="center",
                background_color="white",
                border_radius="2em",
                padding_x="1em",
                height="40px",
            ),
            #spacing="5",
            padding_y="0.5em",
            #height="65px",
            align="center",
            width="100%",
            #justify="between",

        ),
        width="80%",
        background_color="black",
        #box_shadow="0 2px 8px rgba(0,0,0,0.04)",
        #position="sticky",
        #top="0",
        #z_index="100",
        margin_top="2em",
        margin_bottom="2em",
        border_radius="3em",
        padding_left="0.6em",
        padding_right="0.6em",
    )