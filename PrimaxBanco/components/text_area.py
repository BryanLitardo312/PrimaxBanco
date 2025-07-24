import reflex as rx
from ..backend.backend import State

def texto_area(valor,nuevo_valor) -> rx.Component:
    return rx.box(
        rx.text_area(
            placeholder="Ingrese sus comentarios...",
            value=valor,
            on_change=nuevo_valor,
            #color_scheme="gray",
            bg="#3c3c3c",
            max_length=200,
            required=True,
            size="1",
            rows="1",
            style={
                "color": "#fbfbfb",  # Color del texto ingresado
                "::placeholder": {   # Selector correcto para el placeholder
                    "color": "#fbfbfb",
                    "opacity": 1,     # Asegura que el color se vea
                },
            },
        ),
        width="100%",
        height="100%",
        #bg="#3c3c3c",
        border_radius="1em",
    )


def texto_area_rechazo(valor,nuevo_valor) -> rx.Component:
    return rx.box(
        rx.text_area(
            value=valor,
            on_change=nuevo_valor,
            bg="#a4a3a3",
            max_length=200,
            required=True,
            size="1",
            disabled=True,
            style={
                "color": "#fbfbfb",  # Color del texto ingresado
                "::placeholder": {   # Selector correcto para el placeholder
                    "color": "#fbfbfb",
                    "opacity": 1,     # Asegura que el color se vea
                },
            },
        ),
        width="100%",
        border_radius="1em",
        
    )

def upload (icono) -> rx.Component:
    return rx.upload(
        rx.center(
            rx.icon(
                tag=icono,
                size=20,  # Tamaño reducido para caber en 2em
                color=rx.color("gray", 1),
            ),
        ),
        id="upload1",
        bg="#3c3c3c",
        border_radius="0.50em",
        padding="0.7em",
        width="100%",
        height="3em",
        accept={
            "application/pdf": [".pdf"],
        },
    ),

def info(titulo,variable,porcentaje,align) -> rx.Component:
    return rx.vstack(
        rx.text(f"{titulo}",weight="medium",size="2",color="white"),
        rx.box(rx.text(variable,size="1",color="white",align=align), bg="#3c3c3c", padding="0.5em", border_radius="0.5em",width="100%"),
        spacing="1",
        width=porcentaje,
    ),


def match() -> rx.Component:
    return rx.match(
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
        rx.box()
    ),
#{State.novedad_detalle.get('EESS', '')}