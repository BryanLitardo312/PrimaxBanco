import reflex as rx
from ..backend.backend import Novedades, State
from ..components.form_field import form_field
from ..components.status_badges import status_badge
from typing import Optional,List


def show_customer(novedad: dict):
    valor_coment = novedad.get("COMENTARIOS","")
    return rx.table.row(
        #rx.table.cell(novedad.No),
        #rx.table.cell(novedad.id),
        rx.table.cell(novedad.get("EESS", ""),font_size="0.9em"),
        #rx.table.cell(novedad.get("BODEGA", "")),
        rx.table.cell(novedad.get("FECHA", ""),font_size="0.9em"),
        rx.table.cell(novedad.get("LUGAR", ""),font_size="0.9em"),
        rx.table.cell(novedad.get("DETALLE", ""),font_size="0.9em",width="15%",white_space="nowrap"),
        rx.table.cell(novedad.get("SECUENCIAL", ""),font_size="0.9em"),
        rx.table.cell(f'{novedad.get("SIGNO", "")} ${novedad.get("VALOR", "")}',align='center',font_size="0.9em"),
        rx.table.cell(rx.badge(f'#{novedad.get("id", "")}', color_scheme="indigo",variant="solid",style={"fontWeight": "bold", "fontSize": "0.9em"}),align="center",),
        rx.table.cell(
            rx.match(
                novedad.get("STATUS"),
                ("Pendiente", rx.badge("Pendiente", color_scheme="orange",size="2")),
                ("Finalizado", rx.badge("Finalizado", color_scheme="green",size="2")),
                ("Rechazado", rx.badge("Rechazado", color_scheme="tomato",size="2")),
                rx.badge("No aplica", color_scheme="gray",size="2"),                
            ),
            align='center',
            #font_size="0.9em"
        ),
        #rx.table.cell(novedad.get("VALOR", "")),
        #rx.table.cell(novedad.get("DESCRIPCION", "")),
        rx.table.cell(rx.moment(novedad.get("created_at", ""), format="DD/MM/YYYY"),align='center',font_size="0.9em"),
        rx.table.cell(
            rx.hstack(
                rx.cond(
                    State.email == "usuario@bolivariano.com.ec",
                    rx.button(
                        rx.icon("trash-2", size=20),
                        color_scheme="red",
                        variant="ghost",
                        border_radius="3em",
                        size="2",
                        on_click=lambda sec=novedad.get("id", ""): State.borrar_novedad(sec),
                    ),
                    rx.box()  # No muestra nada para otros usuarios
                ),
                rx.link(
                    #rx.text("Ver más...", size="2",high_contrast=True),
                    rx.icon("circle-chevron-right",size=25),
                    #rx.icon
                    href=f"/novedades/{novedad.get("SECUENCIAL", "")}",
                    color_scheme="grass",
                    variant="solid",
                    #size="2",
                ),
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
                    _header_cell("Estacion", "fuel"),
                    _header_cell("Fecha", "calendar-arrow-down"),
                    _header_cell("Matriz", "landmark"),
                    _header_cell("Detalle", "book-text"),
                    _header_cell("Secuencial", "binary"),
                    _header_cell("Valor", "circle-dollar-sign"),
                    _header_cell("Orden", "album"),
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
            rx.button("Anterior",on_click=State.set_page_novedades(State.page_novedades - 1), disabled=State.page_novedades == 1),
            rx.text(f"Página {State.page_novedades}"),
            rx.button("Siguiente", color="white",background_color="black", on_click=State.set_page_novedades(State.page_novedades + 1)),
            justify="center",
            width="100%",
        ),
        justify="center",
        width="100%",
    )
