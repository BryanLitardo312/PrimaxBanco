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
                    width="150px",
                    height="150px",
                    margin_bottom="0.5em",
                ),
                rx.heading("Banca Electrónica", size="5", color="white", margin_bottom="1.5em"),
                #rx.text("Ingreso de credenciales", size="2",color=color_primary, margin_bottom="0.20em"),
                rx.input(
                    placeholder="Correo electrónico",
                    value=State.email,
                    on_change=State.set_email,
                    width="100%",
                    #border=f"1.5px solid {color_border}",
                    #border="1.5px solid",
                    border_radius="md",
                    padding="0.2em",
                    margin_bottom="0.5em",
                    font_size="0.9rem",
                    weight="bold",
                    size="3",
                    background="white",
                ),
                rx.box(height="1em"),
                rx.input(
                    placeholder="Contraseña",
                    type="password",
                    value=State.password,
                    on_change=State.set_password,
                    width="100%",
                    #border=f"1.5px solid {color_border}",
                    #border="1.5px solid",
                    border_radius="md",
                    padding="0.4em",
                    margin_bottom="0.5em",
                    font_size="0.9rem",
                    weight="bold",
                    size="3",
                    background="white",

                ),
                rx.hstack(
                    rx.link(
                        rx.text(
                            "Olvidó su contraseña?",
                            color="white",
                            size="2",
                            style={"textDecoration": "underline", "cursor": "pointer"},
                        ),
                        #href="#",
                        on_click=State.open_dialog,
                        margin_bottom="1em",
                    ),
                    justify="end",
                    width="100%",
                ),
                rx.box(height="0.5em"),
                rx.button(
                    rx.hstack(
                        rx.text("Iniciar sesión",weight="medium"),
                        rx.icon("log-in",size=22, color="grass")
                    ),
                    width="100%",
                    color="white",
                    background="#E96207",
                    #border="2px solid",    
                    size="3",
                    font_weight="bold",
                    margin_bottom="1em",
                    on_click=lambda: State.login(State.email, State.password),  # Aquí iría tu lógica de login
                ),
                rx.box(height="1em"),
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
                rx.dialog.root(
                    rx.dialog.trigger(rx.box()),  # Se puede usar un trigger vacío si abres manualmente
                    rx.dialog.content(
                        rx.vstack(
                            rx.text("Contacte a soporte técnico +593 980849967", size="3", color=color_primary),
                            rx.dialog.close(
                                rx.link(rx.text("Cerrar", size="3"), color_scheme="red",on_click=State.close_dialog)
                            ),
                            align="center",
                        ),
                    ),
                    open=State.show_dialog,
                    #on_open_change=lambda value: State.close_dialog() if not value else None,
                ),
                spacing="1",
                align="center",
                width="360px",
                padding="2.5em",
                #border=f"2px solid {color_border}",
                border_radius="30px",
                background="rgba(255,255,255,0.3)",
                box_shadow="0 4px 24px rgba(0,0,0,0.08)",
                style={
                    "backdropFilter": "blur(12px)",  # Efecto borroso
                    "-webkit-backdrop-filter": "blur(12px)",  # Compatibilidad Safari
                },
            ),
            justify="center",
            align="center",
            #padding_left="15%",
            height="100vh",
            width="100vw",
        ),
        width="100vw",
        min_height="100vh",
        #background_color=color_bg,
        background_image="url('/Puntilla_Nueva.jpg')",
        background_size="cover",
        background_position="center",  # Cambia por la ruta de tu imagen de fondo
    )