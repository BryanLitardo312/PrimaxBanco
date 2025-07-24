import reflex as rx
from ..backend.backend import State
from ..components.text_area import *

#color2 = "rgb(130,130,130)"
#color3 = "#7d0909"
#color4 = "#e4c6c6"

def confirmar_respuesta_novedades():
    return rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button(
            rx.hstack(rx.text("Guardar",color="black"), rx.icon("save-all",color="black")),
            bg='#f0f0f0',
            size="3",
            width="100%",
            #margin_bottom="0.5em",
            margin_top="1.5em",
            style={
                "_hover": {
                    "bg": "#c4c2c2",
                    "color": "#c4c2c2",
                },
                "border-radius": "0.5em",
            },
        ),
    ),
    rx.alert_dialog.content(
        rx.alert_dialog.title("Confirmación"),
        rx.alert_dialog.description(
            "La información se enviará de forma automática, ¿Está seguro de continuar?",
            size="1",
        ),
        rx.flex(
            rx.alert_dialog.cancel(
                rx.button(
                    "Cancelar",
                    variant="soft",
                    color_scheme="gray",
                ),
            ),
            rx.alert_dialog.action(
                rx.button(
                    "Enviar",
                    color_scheme="grass",
                    variant="solid",
                    on_click=State.upload_to_supabase_novedades(
                        rx.upload_files(upload_id="upload1")
                    ),
                ),
            ),
            spacing="3",
            margin_top="16px",
            justify="end",
        ),
        style={"max_width": 400},
    ),
)


@rx.page(route="/novedades/[secuencial]", on_load=State.cargar_novedad)
def novedaddetail() -> rx.Component:
    secuencial = State.router.page.params.get("secuencial", "")
    return rx.box(
        rx.flex(
            rx.vstack(
                rx.image(
                    src="/credit_card.png",
                    width="100%",
                    margin_bottom="0.5em",
                ),
                rx.cond(
                    State.cargando,
                    rx.spinner()
                ),
                rx.box(
                    rx.cond(
                        State.novedad_detalle,
                        rx.vstack(
                            rx.hstack(
                                rx.vstack(
                                    rx.text(f"Estacion",weight="medium",size="2",color="white"),
                                    rx.box(rx.text(f"{State.novedad_detalle.get('EESS', '')}",size="1",color="white"), bg="#3c3c3c", padding="0.5em", border_radius="0.5em",width="100%"),
                                    spacing="1",
                                    width="70%",
                                ),
                                rx.vstack(
                                    rx.text(f"Fecha",weight="medium",size="2",color="white"),
                                    rx.box(rx.text(f"{State.novedad_detalle.get('FECHA', '')}",size="1",color="white",align="center"), bg="#3c3c3c", padding="0.5em", border_radius="0.5em",width="100%"),
                                    spacing="1",
                                    width="30%",
                                ),
                                width="100%",
                            ),
                            rx.hstack(
                                rx.vstack(
                                    rx.text(f"Descripción",weight="medium",size="2",color="white"),
                                    rx.box(rx.text(f"{State.novedad_detalle.get('DETALLE', '')}",size="1",color="white"), bg="#3c3c3c", padding="0.5em", border_radius="0.5em",width="100%"),
                                    spacing="1",
                                    width="70%",
                                ),
                                rx.vstack(
                                    rx.text(f"Monto",weight="medium",size="2",color="white"),
                                    rx.box(rx.text(f"{State.novedad_detalle.get('SIGNO', '')} ${State.novedad_detalle.get('VALOR', '')}",size="1",color="white",align="center"), bg="#3c3c3c", padding="0.5em", border_radius="0.5em",width="100%",),
                                    spacing="1",
                                    width="30%",
                                ),
                                width="100%",
                            ),
                            #rx.box(height="0.5em"),
                            rx.hstack(
                                rx.vstack(
                                    rx.text("Comentarios",weight="medium",size="2",color="white"),
                                    rx.cond(
                                        State.comentario_historial=="",
                                        texto_area(State.comentario,State.set_comentario),
                                        texto_area(State.comentario_historial,State.set_comentario),
                                    ),
                                    spacing="1",
                                    width="85%",
                                    height="100%",
                                ),
                                rx.vstack(
                                    #rx.text("",weight="medium",size="2",color="white"),
                                    upload("upload"),
                                    justify="end",
                                    height="100%",
                                    spacing="1",
                                    width="15%",
                                ),
                            width="100%",
                            align_items='end',
                            ),
                            rx.vstack(
                                rx.cond(
                                    State.comentario_rechazo != "",
                                    rx.vstack(
                                        rx.text(f"Réplica",weight="medium",size="2",color="white"),
                                        texto_area_rechazo(State.comentario_rechazo,State.set_comentario),
                                        spacing="1",
                                        width="100%",
                                    ),
                                ),
                                width="100%",
                            ),
                            rx.hstack(
                                rx.foreach(
                                    rx.selected_files("upload1"),
                                    lambda file: rx.text(file, color="white",size="1",align="center"),
                                ),
                                width="100%",
                                justify="center",
                                align="center",
                            ),
                            #rx.match(
                                #State.upload_status,
                                #("Carga exitosa", rx.badge(
                                    #rx.text(State.upload_status,size="5"),
                                    #variant="soft",
                                    #color_scheme="green",
                                    #size="3",
                                #)),
                                #("Error", rx.badge(
                                    #rx.text(State.upload_status,size="5"),
                                    #variant="soft",
                                    #color_scheme="tomato",
                                    #size="3",
                                #)),
                                #rx.box()
                            #),
                            confirmar_respuesta_novedades(),
                            spacing="3",
                            width="100%",
                        ),
                        rx.spinner(),
                    ),
                    width="100%",
                ),
                spacing="4",
                align="center",
                justify="center",
                width="27em",
                #height="100%",
                padding_x="2.5em",
                padding_y="2.5em",
                #border="2px solid #F4F4F4",
                border_radius="2em",
                background="#212121",
                box_shadow="0 8px 32px rgba(255,255,255,0.38)",
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
        background="linear-gradient(to right, #212121, #212121, #212121)",
        #class_name="bg-gradient-to-r from-gray-100 via-gray-300 to-gray-500 p-8 rounded-lg",
    )