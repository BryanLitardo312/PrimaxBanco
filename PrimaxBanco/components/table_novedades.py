import reflex as rx
from ..backend.backend import Novedades, State
from ..components.form_field import form_field
from ..components.status_badges import status_badge
from typing import Optional,List

def confirmar_borrado(sec):
    return rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button(
            rx.icon("file-x", size=20),
            #rx.text("Delete", size="1", weight="medium"),
            color_scheme="red",
            variant="soft",
            border_radius="1em",
            high_contrast=True,
            size="2",
            #on_click=lambda sec=novedad.get("id", ""): State.borrar_novedad(sec),
        ),
    ),
    rx.alert_dialog.content(
        rx.alert_dialog.title("Confirmación"),
        rx.alert_dialog.description(
            "La información se eliminará permanentemente ¿Está seguro de continuar?",
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
                    "Borrar",
                    color_scheme="red",
                    variant="solid",
                    on_click=State.borrar_novedad(sec),
                ),
            ),
            spacing="3",
            margin_top="16px",
            justify="end",
        ),
        style={"max_width": 400},
    ),
)


def show_customer(novedad: dict):
    valor_coment = novedad.get("COMENTARIOS","")
    return rx.table.row(
        #rx.table.cell(novedad.No),
        #rx.table.cell(novedad.id),
        rx.table.cell(rx.badge(f'#{novedad.get("id", "")}', color_scheme="gray",high_contrast=True,variant="solid",style={"fontWeight": "bold", "fontSize": "1em"}),align="center",),
        rx.table.cell(novedad.get("EESS", ""),font_size="0.9em"),
        #rx.table.cell(novedad.get("BODEGA", "")),
        rx.table.cell(novedad.get("FECHA", ""),font_size="0.9em"),
        rx.table.cell(novedad.get("LUGAR", ""),font_size="0.9em"),
        rx.table.cell(novedad.get("DETALLE", ""),font_size="0.9em",width="15%",white_space="nowrap"),
        rx.table.cell(novedad.get("SECUENCIAL", ""),font_size="0.9em"),
        rx.table.cell(f'{novedad.get("SIGNO", "")} ${novedad.get("VALOR", "")}',align='center',font_size="0.9em"),
        #rx.table.cell(rx.badge(f'#{novedad.get("id", "")}', color_scheme="indigo",variant="solid",style={"fontWeight": "bold", "fontSize": "0.9em"}),align="center",),
        #rx.table.cell(novedad.get("VALOR", "")),
        #rx.table.cell(novedad.get("DESCRIPCION", "")),
        rx.table.cell(rx.moment(novedad.get("created_at", ""), format="DD/MM/YYYY"),align='center',font_size="0.9em"),
        rx.table.cell(
            rx.match(
                novedad.get("STATUS"),
                ("Pendiente", rx.badge("Pendiente", color_scheme="orange",size="3")),
                ("Finalizado", rx.badge("Finalizado", color_scheme="green",size="3")),
                ("Rechazado", rx.badge("Rechazado", color_scheme="tomato",size="3")),
                rx.badge("No aplica", color_scheme="gray",size="3"),                
            ),
            align='center',
            #font_size="0.9em"
        ),
        rx.table.cell(
            rx.hstack(
                rx.cond(
                    State.email == "usuario@bolivariano.com.ec",
                    rx.fragment(
                        confirmar_borrado(novedad.get("id", ""))
                    ),
                    rx.box()  # No muestra nada para otros usuarios
                ),
                rx.link(
                    #rx.text("Ver más...", size="2",high_contrast=True),
                    rx.icon("arrow-right-to-line",size=20),
                    #rx.icon
                    href=f"/novedades/{novedad.get("SECUENCIAL", "")}",
                    color_scheme="indigo",
                    variant="solid",
                    high_contrast=True,
                    #size="2",
                ),
            spacing="1",
            justify="center",
            align="center",
            width="100%",
            ),
            align="center",     
        ),
        background_color="rgb(255,255,255)",
        style={"_hover": {"bg": rx.color("gray", 3)}},
        align="center",
    )


def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=15),
            rx.text(text,size="2", weight="medium"),
            align="center",
            spacing="1",
        ),
        background_color="rgb(0,0,0)",
        style={"color": "white", "fontWeight": "light"},
    )

def main_table():
    
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Orden", "book"),
                    _header_cell("Estacion", "fuel"),
                    _header_cell("Fecha", "calendar-arrow-down"),
                    _header_cell("Matriz", "landmark"),
                    _header_cell("Detalle", "book-text"),
                    _header_cell("Secuencial", "binary"),
                    _header_cell("Valor", "circle-dollar-sign"),
                    _header_cell("Status", "map-pin-house"),
                    _header_cell("Ticket", "calendar-arrow-up"),
                    _header_cell("Actions", "cog"),
                ),
            ),
            #rx.table.body(rx.foreach(State.novedades, show_customer)),
            rx.table.body(rx.foreach(State.novedades, show_customer)),
            variant="surface",
            size="1",
            width="100%",
            on_mount=State.load_entries,
        ),
        rx.hstack(
            rx.cond(
                State.page_novedades == 1,
                rx.button("Anterior", disabled=True),
                rx.button("Anterior", color="white", background_color="black", on_click=State.set_page_novedades(State.page_novedades - 1)),
            ),
            rx.text(f"Página {State.page_novedades}"),
            rx.button("Siguiente", color="white",background_color="black", on_click=State.set_page_novedades(State.page_novedades + 1)),
            justify="center",
            width="100%",
        ),
        justify="center",
        width="100%",
    )
