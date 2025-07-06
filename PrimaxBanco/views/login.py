import reflex as rx
from ..backend.backend import State

color_bg = "#f5f7fa"         # Fondo suave corporativo
color_primary = "#013220"    # Verde corporativo Primax
color_border = "#013220"
color_button = "#009639"     # Botón destacado

@rx.page(route="/",title="Inicio de Sesión",description="Inicia sesión en Primax Banco")
def login():
    return rx.box(
        rx.flex(
            rx.vstack(
                rx.image(
                    src="/primax_logo.png",
                    width="110px",
                    height="110px",
                    margin_bottom="2em",
                ),
                rx.heading("Banca Electrónica", size="5", color=color_primary, margin_bottom="0.4em"),
                rx.text("Ingreso de credenciales", size="2",color=color_primary, margin_bottom="0.20em"),
                rx.input(
                    placeholder="Usuario",
                    value=State.email,
                    on_change=State.set_email,
                    width="100%",
                    border=f"1.5px solid {color_border}",
                    border_radius="md",
                    padding="0.2em",
                    margin_bottom="0.5em",
                    font_size="0.9rem",
                    size="3",
                ),
                rx.input(
                    placeholder="Contraseña",
                    type="password",
                    value=State.password,
                    on_change=State.set_password,
                    width="100%",
                    border=f"1.5px solid {color_border}",
                    border_radius="md",
                    padding="0.4em",
                    margin_bottom="0.5em",
                    font_size="0.9rem",
                    size="3",
                ),
                rx.button(
                    rx.hstack(rx.text("Ingresar"),rx.icon("log-in", size=20, color="white")),
                    width="100%",
                    #color="white",
                    #background=color_button,
                    color_scheme="green",
                    variant="solid",
                    border_radius="md",
                    border=f"1.5px solid",
                    size="3",
                    font_weight="bold",
                    margin_bottom="1.5em",
                    on_click=lambda: State.login(State.email, State.password),  # Aquí iría tu lógica de login
                ),
                rx.cond(
                    State.upload_status_sesion == "Credenciales incorrectas",
                    rx.text(
                        State.upload_status_sesion,
                        color="red",
                        size="2",
                        margin_bottom="1em",
                    ),
                    rx.box(),
                ),
                rx.link(
                    rx.text(
                        "¿Olvidaste tu contraseña?",
                        color=color_primary,
                        size="2",
                        style={"textDecoration": "underline", "cursor": "pointer"},
                    ),
                    #href="#",
                    on_click=State.open_dialog,
                    margin_bottom="1em",
                ),
                rx.dialog.root(
                    rx.dialog.trigger(rx.box()),  # Se puede usar un trigger vacío si abres manualmente
                    rx.dialog.content(
                        rx.vstack(
                            rx.text("Por favor, contacte a Soporte técnico: +593 980849967", size="3", color=color_primary),
                            rx.dialog.close(
                                rx.link(rx.text("Cerrar", size="3"), color_scheme="red",on_click=State.close_dialog)
                                #rx.button(rx.text("Comprendido", size="3"),
                                          #on_click=State.close_dialog,
                                          #color_scheme="grass",
                                          #variat="ghost",
                                          #size="3",)
                            ),
                            align="center",
                        ),
                    ),
                    open=State.show_dialog,
                    #on_open_change=lambda value: State.close_dialog() if not value else None,
                ),
                spacing="4",
                align="center",
                width="360px",
                padding="3em",
                border=f"2px solid {color_border}",
                border_radius="10px",
                background="white",
                box_shadow="0 4px 24px rgba(0,0,0,0.08)",
            ),
            justify="start",
            align="center",
            padding_left="15%",
            height="100vh",
            width="100vw",
        ),
        width="100vw",
        min_height="100vh",
        #background_color=color_bg,
        background_image="url('/portada.jpg')",
        background_size="cover",
        background_position="center",  # Cambia por la ruta de tu imagen de fondo
    )