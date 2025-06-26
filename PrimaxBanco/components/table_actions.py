import reflex as rx
from ..backend.backend import Download, State

def comandos () -> rx.Component:
    return rx.hstack(
            rx.input(
                placeholder="Buscar por código secuencial",
                value=State.codigo_busqueda,
                on_change=lambda value: State.buscar_por_codigo(value),
                width="250px",
            ),
            rx.spacer(),
            rx.select(
                ["Pendiente", "Finalizado", "Rechazado"],
                placeholder="Filtrar por estado",
                on_change=lambda value: State.load_entries(value),
            ),
            rx.button(
                rx.hstack(
                    rx.icon("download", size=20),
                    rx.text("Descargar", size="2"),
                ),
                on_click=Download.descargar_novedades_csv,
                color_scheme="blue",
                size="2",
            ),
            width="81%",
            align="center",
            #align="stretch",
        ),