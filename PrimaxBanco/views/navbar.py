import reflex as rx
from ..backend.backend import State


def navbar():
    return rx.box(
        rx.hstack(
            # Logo a la izquierda
            rx.box(
                rx.image(
                src="/primax_logo.png",
                width="auto",
                height="35px",
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
                        size="3",
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
                        size="3",
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
                        size="3",
                        style={
                            "color": "white",
                            "fontWeight": "medium",
                            "transition": "all 0.2s ease-in-out",
                            "_hover": {
                                "transform": "scale(1.20)",
                            },
                        },
                    ),
                    href="/suministros",
                ),
                rx.link(
                    rx.text(
                        "Devoluciones",
                        size="3",
                        style={
                            "color": "white",
                            "fontWeight": "medium",
                            "transition": "all 0.2s ease-in-out",
                            "_hover": {
                                "transform": "scale(1.20)",
                            },
                        },
                    ),
                    href="/devoluciones",
                ),
                spacing="9",
                justify="between",
                width="60%",
            ),
            rx.spacer(),
            rx.box(
                rx.text(State.email),
                style={"fontWeight": "medium", "color": "grey"},
                display="flex",
                background_color="white",
                border_radius="2em",
                padding_x="2em",
                height="35px",
                #display=["none", "none", "block"],
                align_items="center",
            ),
            rx.box(
                rx.button(
                    rx.icon(tag="log-out", size=22),
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
                padding_x="1.5em",
                height="35px",
            ),
            #spacing="5",
            padding_y="0.6em",
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
        padding_left="0.7em",
        padding_right="0.7em",
    )



def navbar_mobile():
    return rx.box(
        rx.hstack(
            rx.spacer(),
            rx.hstack(
                rx.link(
                    rx.icon(
                        "Home",
                        size=25,
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
                    rx.icon(
                        "landmark",
                        size=25,
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
                    rx.icon(
                        "truck",
                        size=25,
                        style={
                            "color": "white",
                            "fontWeight": "medium",
                            "transition": "all 0.2s ease-in-out",
                            "_hover": {
                                "transform": "scale(1.20)",
                            },
                        },
                    ),
                    href="/suministros",
                ),
                rx.link(
                    rx.icon(
                        "book",
                        size=25,
                        style={
                            "color": "white",
                            "fontWeight": "medium",
                            "transition": "all 0.2s ease-in-out",
                            "_hover": {
                                "transform": "scale(1.20)",
                            },
                        },
                    ),
                    href="/devoluciones",
                ),
                spacing="9",
                justify="between",
                width="60%",
            ),
            rx.spacer(),
            rx.box(
                rx.button(
                    rx.icon(tag="log-out", size=22),
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
                padding_x="1.5em",
                height="35px",
            ),
            #spacing="5",
            padding_y="0.6em",
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
        padding_left="0.7em",
        padding_right="0.7em",
    )