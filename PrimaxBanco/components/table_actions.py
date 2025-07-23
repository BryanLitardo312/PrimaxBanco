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
                width="50%",
                height="2.3em",
            ),
            rx.spacer(),
            rx.select(
                ["Todos", "Pendiente", "Finalizado", "Rechazado"],
                placeholder="Filtrar por estado",
                on_change=lambda value: State.load_entries(value),
                color_scheme="gray",
                high_contrast=True,
                variant="soft",
                width="15em",
            ),
            rx.button(
                rx.hstack(
                    rx.icon("download", size=20),
                    #rx.text("Descargar", size="2"),
                ),
                on_click=Download.descargar_novedades_csv,
                #bg="#018014",
                color_scheme="grass",
                variant="outline",
                border_radius="30%",
                size="2",
            ),
            width="85%",
            align="center",
            #align="stretch",
        ),

def comandos_suministros () -> rx.Component:
    return rx.hstack(
            rx.input(
                rx.input.slot(
                    rx.icon(tag="search"),
                ),
                placeholder="Buscar por estación",
                value=State.estacion_busqueda,
                on_change=lambda value: State.buscar_por_estacion(value),
                width="50%",
                height="2.3em",
            ),
            rx.spacer(),
            rx.select(
                ["Todos", "Pendiente", "Finalizado", "Rechazado"],
                placeholder="Filtrar por estado",
                on_change=lambda value: State.load_suministros(value),
                color_scheme="gray",
                high_contrast=True,
                variant="soft",
                width="15em",
            ),
            rx.button(
                rx.hstack(
                    rx.icon("download", size=30),
                    #rx.text("Descargar", size="2"),
                ),
                on_click=Download.descargar_suministros_csv,
                color_scheme="gray",
                size="2",
            ),
            width="85%",
            align="center",
            #align="stretch",
        ),


def comandos_devoluciones () -> rx.Component:
    return rx.hstack(
            rx.input(
                rx.input.slot(
                    rx.icon(tag="search"),
                ),
                placeholder="Buscar por secuencial",
                value=State.codigo_busqueda_devoluciones,
                on_change=lambda value: State.buscar_por_codigo_devoluciones(value),
                width="50%",
                height="2.3em",
            ),
            rx.spacer(),
            rx.select(
                ["Todos", "Pendiente", "Finalizado", "Rechazado"],
                placeholder="Filtrar por estado",
                on_change=lambda value: State.load_devoluciones(value),
                color_scheme="gray",
                high_contrast=True,
                variant="soft",
                width="15em",
            ),
            rx.button(
                rx.hstack(
                    rx.icon("download", size=30),
                    #rx.text("Descargar", size="2"),
                ),
                on_click=Download.descargar_devoluciones_csv,
                color_scheme="gray",
                size="2",
            ),
            width="85%",
            align="center",
            #align="stretch",
        ),
