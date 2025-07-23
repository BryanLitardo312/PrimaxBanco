import reflex as rx
from ..backend.backend import State
                
color_letra="#0A0A0A"
color_letra2="#010159"


def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon,color="#474b4b",size=25),
            rx.text(text, color="#474b4b",size="3", weight="medium"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": "white",
                    "color": "#828282",
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Novedades", "layout-dashboard", "/novedades"),
        sidebar_item("Suministros", "square-library", "/suministros"),
        sidebar_item("Devoluciones", "bar-chart-4", "/devoluciones"),
        sidebar_item("Quejas", "mail", "/devoluciones"),
        spacing="2",
        width="100%",
    )


def sidebar_bottom_profile() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.card(
                        rx.image(
                        src="/primax_logo.png",
                        width="9em",
                        height="auto",
                        #border_radius="50%",
                        background_color="white",
                        ),
                        border_radius="20%",
                        box_shadow="0 4px 24px rgba(0,0,0,0.28)",
                    ),
                    
                    align="center",
                    justify="center",
                    padding_x="0.5rem",
                    width="100%",
                ),
                rx.box(height="1.5em"),
                sidebar_items(),
                rx.spacer(),
                rx.vstack(
                    rx.divider(height="3px"),
                    rx.hstack(
                        rx.icon_button(
                            rx.icon("user"),
                            size="3",
                            radius="full",
                            color="black",
                            background_color="white",
                        ),
                        rx.vstack(
                            rx.box(
                                rx.text(
                                    "Mi cuenta",
                                    size="2",
                                    weight="bold",
                                    color="474b4b",
                                ),
                                rx.text(
                                    State.email,
                                    size="1",
                                    weight="medium",
                                    color="474b4b",
                                ),
                                width="100%",
                            ),
                            spacing="0",
                            align="start",
                            justify="start",
                            width="100%",
                        ),
                        padding_x="0.5rem",
                        align="center",
                        justify="start",
                        width="100%",
                    ),
                    rx.vstack(
                        #sidebar_item(
                            #"Settings", "settings", "/#"
                        #),
                        rx.button(
                            rx.hstack(
                                rx.icon("log-out",size=20,border_color="black"),
                                rx.text("Cerrar sesión", size="2",weight="medium"),
                                spacing="1",
                                #background_color=rx.color("gray",9),
                            ),
                            background_color="#0D0D0D",
                            on_click=State.logout,
                            width="100%",
                            padding_x="0.5rem",
                            padding_y="0.75rem",
                            align="center",
                            style={
                                "_hover": {
                                    "bg": "#c20808",
                                    "color": "white",
                                },
                                "border-radius": "2em",
                            },
                        ),
                        spacing="1",
                        width="100%",
                    ),
                    width="100%",
                    spacing="5",
                ),
                spacing="5",
                # position="fixed",
                left="0px",
                top="0px",

                #z_index="5",
                padding_x="1em",
                padding_y="1.5em",
                bg="rgb(245, 245, 245)",
                align="start",
                width="17em",
                height="100vh",  # Altura completa de la ventana
                position="sticky",  # Opcional: sidebar fijo
                
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                            ),
                            sidebar_items(),
                            rx.spacer(),
                            rx.vstack(
                                rx.vstack(
                                    sidebar_item(
                                        "Settings",
                                        "settings",
                                        "/#",
                                    ),
                                    sidebar_item(
                                        "Log out",
                                        "log-out",
                                        "/#",
                                    ),
                                    width="100%",
                                    spacing="1",
                                ),
                                rx.divider(margin="0"),
                                rx.hstack(
                                    rx.icon_button(
                                        rx.icon("user"),
                                        size="3",
                                        radius="full",
                                    ),
                                    rx.vstack(
                                        rx.box(
                                            rx.text(
                                                "My account",
                                                size="3",
                                                weight="bold",
                                            ),
                                            rx.text(
                                                State.email,
                                                size="2",
                                                weight="medium",
                                            ),
                                            width="100%",
                                        ),
                                        spacing="0",
                                        justify="start",
                                        width="100%",
                                    ),
                                    padding_x="0.5rem",
                                    align="center",
                                    justify="start",
                                    width="100%",
                                ),
                                width="100%",
                                spacing="5",
                            ),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg="#edebeb",
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
        text_overflow="ellipsis",
        overflow="hidden",
    )