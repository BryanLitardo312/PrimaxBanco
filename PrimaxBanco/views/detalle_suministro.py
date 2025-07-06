import reflex as rx
from ..backend.backend import State
from datetime import datetime

color2 = "rgb(130,130,130)"


@rx.page(route="/suministros/[request]", on_load=State.cargar_suministro)
def suministrodetail() -> rx.Component:
    request = State.router.page.params.get("request", "")
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
                rx.cond(
                    State.cargando,
                    rx.spinner()
                ),
                rx.cond(
                    State.suministro_detalle,
                    rx.vstack(
                        rx.hstack(
                            rx.text(f"Orden: #",weight="medium",size="3"),
                            rx.text(f"{request}",size="2",),
                            align="center",
                        ),
                        rx.hstack(
                            rx.text(f"Estación:",weight="medium",size="3"),
                            rx.text(f"{State.suministro_detalle.get('bodega', '')}-{State.suministro_detalle.get('estacion', '')}",size="2"),
                            align="center",
                        ),
                        rx.hstack(
                            rx.text(f"Fecha:",weight="medium",size="3"),
                            rx.text(rx.moment(State.suministro_detalle.get("created_at", ""), format="DD/MM/YYYY"),size="2"),
                            align="center",
                            #rx.text(f"{State.suministro_detalle.get('created_at_formateada', '')}", size="2"),
                        ),
                        rx.hstack(
                            rx.text(f"Descripción:",weight="medium",size="3"),
                            rx.text(f"{State.suministro_detalle.get('detalle', '')}",size="2"),
                            align="center",
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
                        #style={"border-color" : "black",
                               #"border" : f"1px dotted {color2}"},
                        border=f"2px solid {color2}",
                        height="100%",
                        size="3",
                    ),
                    width="90%",
                    #height="30%",
                ),
                rx.box(
                    rx.upload(
                        rx.vstack(
                            rx.icon(
                                tag="files",
                                size=35,
                                color="grey",
                            ),
                            justify="center",
                            align="center",
                            height="100%",
                        ),
                        id="upload1",
                        border=f"2px solid {color2}",
                        border_radius="10px 10px",
                        padding="1.3em",
                        height="100%",
                        accept={
                            "application/pdf": [".pdf"],
                        },
                        #style={"border-color" : "black",
                               #"border" : f"1px dotted {color2}"},
                    ),
                    #height="50px",
                    width="90%",
                ),
                rx.hstack(
                    rx.foreach(
                        rx.selected_files("upload1"), rx.text
                    )
                ),
                rx.button(
                    rx.hstack(rx.icon("mail"), rx.text("Enviar")),
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
            #padding_y="1em",
        ),
        height="100vh",
        #background_color=color_bg,
        #class_name="bg-gradient-to-r from-pink-200 via-yellow-200 to-orange-200 p-8 rounded-lg"
        class_name="bg-gradient-to-r from-gray-100 via-gray-300 to-gray-500 p-8 rounded-lg",
    ),
