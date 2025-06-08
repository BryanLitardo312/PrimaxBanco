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
        rx.table.cell(f'{novedad.get("SIGNO", "")} {novedad.get("VALOR", "")}',align='right'),
        rx.table.cell(
            rx.cond(
                valor_coment=="",
                rx.badge("Pendiente", color_scheme="orange"),
                rx.badge("Finalizado", color_scheme="green"),
                #rx.icon("x", color="red", size=18),
                #rx.icon("check", color="green", size=18),
                
            ),
            align='center'
        ),
        #rx.table.cell(novedad.get("VALOR", "")),
        #rx.table.cell(novedad.get("DESCRIPCION", "")),
        rx.table.cell(rx.moment(novedad.get("created_at", ""), format="DD/MM/YYYY"),align='center'),
        #rx.table.cell(novedad.get("created_at", "")),
        #rx.table.cell(
            #rx.match(
                #user.status,
                #("Delivered", status_badge("Delivered")),
                #("Pending", status_badge("Pending")),
                #("Cancelled", status_badge("Cancelled")),
                #status_badge("Pending"),
            #)
        #),
        rx.table.cell(
            rx.link(
                rx.text("Ver más...", size="2",high_contrast=True),
                href=f"/tabla/{novedad.get("SECUENCIAL", "")}",
                color_scheme="blue",
                variant="solid",
                size="2",
            ),       
        ),
        background_color="rgb(255,255,255)",
        style={"_hover": {"bg": rx.color("gray", 3)}},
        align="center",
    )


def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text,size="3", weight="bold"),
            align="center",
            spacing="2",
        ),
        background_color="rgb(255,255,255)",
        style={"color": "black", "fontWeight": "bold"},
    )

def main_table():
    
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Estacion", "user"),
                    #_header_cell("Estación", "mail"),
                    _header_cell("Fecha", "phone"),
                    _header_cell("Lugar", "home"),
                    _header_cell("Detalle", "dollar-sign"),
                    _header_cell("Secuencial", "calendar"),
                    #_header_cell("Signo", "truck"),
                    _header_cell("Valor", "cog"),
                    #_header_cell("Descripción", "home"),
                    _header_cell("Creación Ticket", "dollar-sign"),
                    #_header_cell("Date", "calendar"),
                    _header_cell("Status", "truck"),
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
