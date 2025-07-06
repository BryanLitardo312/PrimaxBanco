import reflex as rx
from ..backend.backend import State

color2 = "rgb(130,130,130)"


@rx.page(route="/novedades/[secuencial]", on_load=State.cargar_novedad)
def novedaddetail() -> rx.Component:
    secuencial = State.router.page.params.get("secuencial", "")
    return rx.box(
        rx.flex(
            rx.vstack(
                rx.image(
                    src="/primax_logo.png",
                    width="100px",
                    height="100px",
                    margin_bottom="1em",
                    #margin_top="0.5em",
                ),
                #rx.heading(f"Soportes bancarios", size="7"),
                # Estado de carga
                rx.cond(
                    State.cargando,
                    rx.spinner()
                ),
                # Mensaje de error
                rx.cond(
                    State.error,
                    rx.text(State.error, color="red")
                ),
                # Mostrar datos si existen
                rx.cond(
                    State.novedad_detalle,
                    rx.vstack(
                        rx.hstack(
                            rx.text(f"Novedad:",weight="medium",size="3"),
                            rx.text(f"{secuencial}",size="2"),
                        ),
                        rx.hstack(
                            rx.text(f"Estación:",weight="medium",size="3"),
                            rx.text(f"{State.novedad_detalle.get('BODEGA', '')}-{State.novedad_detalle.get('EESS', '')}",size="2"),
                        ),
                        rx.hstack(
                            rx.text(f"Fecha:",weight="medium",size="3"),
                            rx.text(f"{State.novedad_detalle.get('FECHA', '')}",size="2"),
                        ),
                        rx.hstack(
                            rx.text(f"Descripción:",weight="medium",size="3"),
                            rx.text(f"{State.novedad_detalle.get('DETALLE', '')}",size="2"),
                        ),
                        rx.hstack(
                            rx.text(f"Valor:",weight="medium",size="3"),
                            rx.text(f"{State.novedad_detalle.get('SIGNO', '')} ${State.novedad_detalle.get('VALOR', '')}",size="3"),
                        ),
                        spacing="1"
                    )
                ),
                rx.box(height="1em"),
                rx.box(
                    rx.text_area(
                        placeholder="Ingrese sus comentarios...",
                        value=State.comentario,
                        on_change=State.set_comentario,
                        #on_blur=TextAreaBlur.set_text,
                        #radius="large",
                        border_radius="10px 10px",
                        max_length=200,
                        required=True,
                        border=f"2px solid {color2}",
                        height="100%",
                        size="3",
                        style={
                            "& textarea": {
                                "color": "blue"
                            }
                        }
                    ),
                    width="90%",
                    #height="30%",
                ),
                rx.box(
                    rx.cond(
                        State.comentario == "",
                        rx.upload(
                            rx.vstack(
                                rx.icon(
                                    tag="files",
                                    size=45,
                                    #color="grey",
                                    color=rx.color("gray",11),
                                ),
                                justify="center",
                                align="center",
                                height="100%",
                            ),
                            id="upload1",
                            bg="#f0f0f0",
                            border=f"2px solid {color2}",
                            border_radius="10px 10px",
                            padding="1.3em",
                            height="100%",
                            accept={
                                "application/pdf": [".pdf"],
                            },
                        ),
                        rx.upload(
                            rx.vstack(
                                rx.icon(
                                    tag="files",
                                    size=25,
                                    color=rx.color("gray",11),
                                ),
                                rx.text('Documento cargado'),
                                justify="center",
                                align="center",
                                height="100%",
                            ),
                            id="upload1",
                            bg="#f0f0f0",
                            border=f"2px solid {color2}",
                            border_radius="10px 10px",
                            padding="1.3em",
                            height="100%",
                            accept={
                                "application/pdf": [".pdf"],
                            },
                        ),
                    ),
                    width="90%",
                ),
                rx.hstack(
                    rx.foreach(
                        rx.selected_files("upload1"), rx.text
                    )
                ),
                rx.button(
                    rx.hstack(rx.text("Actualizar"), rx.icon("recycle")),
                    on_click=State.upload_to_supabase_novedades(
                        rx.upload_files(upload_id="upload1")
                    ),
                    color_scheme="grass",
                    size="3",
                    width="90%",
                    margin_bottom="2em",
                    margin_top="1em",
                ),
                
                spacing="4",
                align="center",
                justify="center",
                width="23em",
                height="100%",
                padding_x="2em",
                padding_y="2em",
                border_radius="1.5em",
                background="white",
                box_shadow="0 8px 32px rgba(0,0,0,0.08)",
            ),
            width="100%",
            justify="center",
            align="center",
            padding_x="2.5em",
            padding_top="2em",
        ),
        height="100vh",
        #background_color=color_bg,
        #class_name="bg-gradient-to-r from-pink-200 via-yellow-200 to-orange-200 p-8 rounded-lg"
        background="linear-gradient(to right, #f3f4f6, #d1d5db, #6b7280)",
        #class_name="bg-gradient-to-r from-gray-100 via-gray-300 to-gray-500 p-8 rounded-lg",
    ),
