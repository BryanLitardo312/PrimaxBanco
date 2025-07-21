import reflex as rx
from ..backend.backend import State

color2 = "rgb(130,130,130)"
color3 = "#7d0909"
color4 = "#e4c6c6"

@rx.page(route="/devoluciones/[secuencial]", on_load=State.cargar_devolucion)
def devoluciondetail() -> rx.Component:
    secuencial = State.router.page.params.get("secuencial", "")
    return rx.box(
        rx.flex(
            rx.vstack(
                rx.image(
                    src="/primax_logo.png",
                    width="100px",
                    height="100px",
                    margin_bottom="1em",
                ),
                rx.cond(
                    State.cargando,
                    rx.spinner()
                ),
                # Mostrar datos si existen
                rx.box(
                    rx.cond(
                        State.devolucion_detalle,
                        rx.vstack(
                            rx.hstack(
                                rx.text(f"Novedad:",weight="medium",size="2"),
                                rx.text(f"{secuencial}",size="2"),
                            ),
                            rx.hstack(
                                rx.text(f"Estación:",weight="medium",size="2"),
                                rx.text(f"{State.devolucion_detalle.get('BODEGA', '')}-{State.devolucion_detalle.get('EESS', '')}",size="2"),
                            ),
                            rx.hstack(
                                rx.text(f"Fecha:",weight="medium",size="2"),
                                rx.text(f"{State.devolucion_detalle.get('FECHA', '')}",size="2"),
                            ),
                            rx.vstack(
                                rx.text(f"Descripción:",weight="medium",size="2"),
                                rx.text(f"{State.devolucion_detalle.get('DETALLE', '')}",size="2"),
                                spacing="0",
                            ),
                            rx.hstack(
                                rx.text(f"Valor:",weight="medium",size="2"),
                                rx.text(f"{State.devolucion_detalle.get('SIGNO', '')} ${State.devolucion_detalle.get('VALOR', '')}",size="2"),
                            ),
                            spacing="1"
                        )
                    ),
                    width="100%",
                ),
                rx.cond(
                    State.comentario_rechazo == "",
                    rx.box(height="1em"),
                    rx.vstack(
                        rx.box(height="1em"),
                        rx.box(
                            rx.vstack(
                                rx.text(f"Rechazado por:",weight="medium", size="2",color="#060606"),
                                rx.text(f"{State.comentario_rechazo}", size="2",color="#060606"),
                            ),
                            width="100%",
                            border_radius="10px 10px",
                            border=f"2px solid {color3}",
                            background_color=color4,
                            padding="0.75em"
                        ),
                    width="90%",
                    ),
                ),
                rx.box(
                    rx.cond(
                        State.comentario_historial == "",
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
                        ),
                        rx.text_area(
                            placeholder="Ingrese sus comentarios...",
                            value=State.comentario_historial,
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
                                    "color": "#7d0909"
                                }
                            }
                        ),
                    ),
                    width="90%",
                ),
                rx.box(
                    rx.cond(
                        State.comentario_historial == "",
                        rx.upload(
                            rx.vstack(
                                rx.icon(
                                    tag="folder-up",
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
                                    tag="folder-x",
                                    size=30,
                                    color="#f0f0f0",
                                ),
                                rx.text('Documento cargado'),
                                justify="center",
                                align="center",
                                height="100%",
                            ),
                            id="upload1",
                            bg="#b6b4b4",
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
                rx.match(
                    State.upload_status,
                    ("Carga exitosa", rx.badge(
                        rx.text(State.upload_status,size="5"),
                        variant="soft",
                        color_scheme="green",
                        size="3",
                    )),
                    ("Error", rx.badge(
                        rx.text(State.upload_status,size="5"),
                        variant="soft",
                        color_scheme="tomato",
                        size="3",
                    )),
                    rx.box(height="0.5em")
                ),
                rx.button(
                    rx.hstack(rx.text("Actualizar"), rx.icon("recycle")),
                    on_click=State.upload_to_supabase_devoluciones(
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
                #height="100%",
                padding_x="2em",
                padding_y="2em",
                border_radius="1.5em",
                background="white",
                box_shadow="0 8px 32px rgba(0,0,0,0.08)",
            ),
            width="100%",
            justify="center",
            align="center",
            padding_top="2em",
            margin_bottom="2em",
        ),
        height="100vh",
        min_height="100vh",
        overflow_y="auto",
        background="linear-gradient(to right, #f3f4f6, #d1d5db, #6b7280)",
        #class_name="bg-gradient-to-r from-pink-200 via-yellow-200 to-orange-200 p-8 rounded-lg"
        #class_name="bg-gradient-to-r from-gray-100 via-gray-300 to-gray-500 p-8 rounded-lg",
    ),
