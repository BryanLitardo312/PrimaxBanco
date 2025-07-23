import reflex as rx
from ..backend.backend import State

color2 = "rgb(130,130,130)"
color3 = "#7d0909"
color4 = "#e4c6c6"

@rx.page(route="/novedades/[secuencial]", on_load=State.cargar_novedad)
def novedaddetail() -> rx.Component:
    secuencial = State.router.page.params.get("secuencial", "")
    return rx.box(
        rx.flex(
            rx.vstack(
                rx.image(
                    src="/credit_card.png",
                    width="100%",
                    margin_bottom="0.7em",

                ),
                rx.cond(
                    State.cargando,
                    rx.spinner()
                ),
                rx.box(height="1em"),
                rx.box(
                    rx.cond(
                        State.novedad_detalle,
                        rx.vstack(
                            rx.hstack(
                                rx.vstack(
                                    rx.text(f"Estacion",weight="medium",size="2",color="white"),
                                    rx.box(rx.text(f"{State.novedad_detalle.get('EESS', '')}",size="2",color="white"), bg="#3c3c3c", padding="0.5em", border_radius="0.5em",width="100%"),
                                    spacing="1",
                                    width="60%",
                                ),
                                rx.vstack(
                                    rx.text(f"Fecha",weight="medium",size="2",color="white"),
                                    rx.box(rx.text(f"{State.novedad_detalle.get('FECHA', '')}",size="2",color="white",align="center"), bg="#3c3c3c", padding="0.5em", border_radius="0.5em",width="100%"),
                                    spacing="1",
                                    width="40%",
                                ),
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text(f"Descripción",weight="medium",size="2",color="white"),
                                rx.box(rx.text(f"{State.novedad_detalle.get('DETALLE', '')}",size="2",color="white"), bg="#3c3c3c", padding="0.5em", border_radius="0.5em",width="100%"),
                                spacing="1",
                                width="100%",
                            ),
                            rx.hstack(
                                rx.vstack(
                                    rx.text(f"Secuencial",weight="medium",size="2",color="white"),
                                    rx.box(rx.text(f"{State.novedad_detalle.get('SECUENCIAL', '')}",size="2",color="white"), bg="#3c3c3c", padding="0.5em", border_radius="0.5em",width="100%"),
                                    spacing="1",
                                    width="60%",
                                ),
                                rx.vstack(
                                    rx.text(f"Monto",weight="medium",size="2",color="white"),
                                    rx.box(rx.text(f"{State.novedad_detalle.get('SIGNO', '')} ${State.novedad_detalle.get('VALOR', '')}",size="2",color="white",align="center"), bg="#3c3c3c", padding="0.5em", border_radius="0.5em",width="100%",),
                                    spacing="1",
                                    width="40%",
                                ),
                                width="100%",
                            ),
                            rx.box(height="1em"),
                            rx.vstack(
                                rx.text("Mi comentario",weight="medium",size="2",color="white"),
                                rx.box(
                                    rx.cond(
                                        State.comentario_historial == "",
                                        rx.text_area(
                                            placeholder="Ingrese sus comentarios...",
                                            value=State.comentario,
                                            on_change=State.set_comentario,
                                            bg="#3c3c3c",
                                            max_length=200,
                                            required=True,
                                            height="100%",
                                            size="3",
                                            style={
                                                "& textarea": {
                                                    "color": "#fbfbfb"
                                                },
                                                "&::placeholder": {  # <-- Estilo para el placeholder
                                                    "color": "#fbfbfb",  # Color gris claro
                                                    "opacity": 1,  # Asegura que no sea semitransparente
                                                },
                                            }
                                        ),
                                        rx.text_area(
                                            placeholder="Ingrese sus comentarios...",
                                            value=State.comentario_historial,
                                            on_change=State.set_comentario,
                                            bg="#3c3c3c",
                                            max_length=200,
                                            required=True,
                                            height="100%",
                                            size="3",
                                            style={
                                                "& textarea": {
                                                    "color": "#fbfbfb"
                                                },
                                                "&::placeholder": {  # <-- Estilo para el placeholder
                                                    "color": "#fbfbfb",  # Color gris claro
                                                    "opacity": 1,  # Asegura que no sea semitransparente
                                                },
                                            },
                                        ),
                                    ),
                                    width="100%",
                                    bg="#3c3c3c",
                                    border_radius="2em",
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.cond(
                                    State.comentario_rechazo != "",
                                    rx.vstack(
                                        rx.text(f"Réplica",weight="medium",size="2",color="white"),
                                        rx.box(
                                            rx.text(f"{State.comentario_rechazo}", size="2",color="white"), 
                                            width="100%",
                                            height="5em",
                                            border_radius="0.50em",
                                            padding="0.5em",
                                            background_color="#3c3c3c",
                                        ),
                                    width="100%",
                                    ),
                                ),
                                width="100%",
                            ),
                            rx.text(f"Soportes",weight="medium",size="2",color="white"),
                            rx.box(
                                rx.cond(
                                    State.comentario_historial == "",
                                    rx.upload(
                                        rx.vstack(
                                            rx.icon(
                                                tag="upload",
                                                size=45,
                                                color=rx.color("gray",1),
                                            ),
                                            justify="center",
                                            align="center",
                                            height="100%",
                                        ),
                                        id="upload1",
                                        bg="#3c3c3c",
                                        border_radius="0.50em",
                                        padding="1.5em",
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
                                            rx.text('¿Volver a cargar el archivo?', size="3", color="#f0f0f0"),
                                            justify="center",
                                            align="center",
                                            height="100%",
                                        ),
                                        id="upload1",
                                        bg="#3c3c3c",
                                        border_radius="0.50em",
                                        padding="1.5em",
                                        height="100%",
                                        accept={
                                            "application/pdf": [".pdf"],
                                        },
                                    ),
                                ),
                                width="100%",
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
                                on_click=State.upload_to_supabase_novedades(
                                    rx.upload_files(upload_id="upload1")
                                ),
                                bg='#0b6730',
                                size="3",
                                width="100%",
                                margin_bottom="3em",
                                margin_top="1em",
                            ),
                            spacing="3"
                        ),
                    ),
                    width="100%",
                ),
                
                spacing="4",
                align="center",
                justify="center",
                width="28em",
                #height="100%",
                padding_x="2em",
                padding_y="2em",
                #border="2px solid #F4F4F4",
                border_radius="1.5em",
                background="#212121",
                box_shadow="0 8px 32px rgba(255,255,255,0.28)",
            ),
            width="100%",
            justify="center",
            align="center",
            #padding_x="2.5em",
            padding_top="2em",
            margin_bottom="2em",
        ),
        min_height="100vh",
        overflow_y="auto",
        #class_name="bg-gradient-to-r from-pink-200 via-yellow-200 to-orange-200 p-8 rounded-lg"
        background="linear-gradient(to right, #71717a, #212121, #212121)",
        #class_name="bg-gradient-to-r from-gray-100 via-gray-300 to-gray-500 p-8 rounded-lg",
    ),
