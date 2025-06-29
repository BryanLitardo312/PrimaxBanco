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
        rx.table.cell(novedad.get("EESS", "")),
        #rx.table.cell(novedad.get("BODEGA", "")),
        rx.table.cell(novedad.get("FECHA", "")),
        rx.table.cell(novedad.get("LUGAR", "")),
        rx.table.cell(novedad.get("DETALLE", "")),
        rx.table.cell(novedad.get("SECUENCIAL", "")),
        rx.table.cell(f'{novedad.get("SIGNO", "")} ${novedad.get("VALOR", "")}',align='center'),
        rx.table.cell(rx.badge(f'#{novedad.get("id", "")}', color_scheme="gray",variant="solid",size="3"),align="center",style={"fontWeight": "bold", "size": "2em"}),
        rx.table.cell(
            rx.match(
                novedad.get("STATUS"),
                ("Pendiente", rx.badge("Pendiente", color_scheme="orange",size="3")),
                ("Finalizado", rx.badge("Finalizado", color_scheme="green",size="3")),
                ("Rechazado", rx.badge("Rechazado", color_scheme="tomato",size="3")),
                rx.badge("No aplica", color_scheme="gray",size="3"),                
            ),
            align='center'
        ),
        #rx.table.cell(novedad.get("VALOR", "")),
        #rx.table.cell(novedad.get("DESCRIPCION", "")),
        rx.table.cell(rx.moment(novedad.get("created_at", ""), format="DD/MM/YYYY"),align='center'),
        rx.table.cell(
            rx.hstack(
                rx.cond(
                    State.email == "usuario@bolivariano.com.ec",
                    rx.button(
                        rx.icon("trash-2", size=25),
                        color_scheme="red",
                        variant="ghost",
                        size="3",
                        on_click=lambda sec=novedad.get("id", ""): State.borrar_novedad(sec),
                    ),
                    rx.box()  # No muestra nada para otros usuarios
                ),
                rx.link(
                    #rx.text("Ver más...", size="2",high_contrast=True),
                    rx.icon("circle-chevron-right",size=30),
                    #rx.icon
                    href=f"/tabla/{novedad.get("SECUENCIAL", "")}",
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
            rx.icon(icon, size=18),
            rx.text(text,size="3"),
            align="center",
            spacing="2",
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
            rx.button("Anterior", on_click=State.set_page(State.page - 1), disabled=State.page == 1),
            rx.text(f"Página {State.page}"),
            rx.button("Siguiente", on_click=State.set_page(State.page + 1)),
            justify="center",
            width="100%",
        ),
        justify="center",
        width="90%",
    )
