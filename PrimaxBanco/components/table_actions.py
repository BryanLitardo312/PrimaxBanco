import reflex as rx
from ..backend.backend import Download, State

def filtrar_estado(value):
    return None if value == "Todos" else value

def comandos () -> rx.Component:
    return rx.hstack(
            rx.input(
                rx.input.slot(
                    rx.icon(tag="search"),
                ),
                placeholder="Buscar por secuencial",
                value=State.codigo_busqueda,
                on_change=lambda value: State.buscar_por_codigo(value),
                width="35em",
                height="2.5em",
            ),
            rx.spacer(),
            rx.select(
                ["Todos", "Pendiente", "Finalizado", "Rechazado"],
                placeholder="Filtrar por estado",
                on_change=lambda value: State.load_entries(value),
            ),
            rx.button(
                rx.hstack(
                    rx.icon("download", size=20),
                    rx.text("Descargar", size="2"),
                ),
                on_click=Download.descargar_novedades_csv,
                color_scheme="grass",
                size="2",
            ),
            width="81%",
            align="center",
            #align="stretch",
        ),