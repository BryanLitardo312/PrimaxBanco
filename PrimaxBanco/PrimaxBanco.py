import reflex as rx

from .components.stats_cards_novedades import stats_cards_group
from .views.navbar import navbar
from .views.login import login
from .views.novedades import Novedades
from .views.detalle_novedad import novedaddetail
from .views.detalle_suministro import suministrodetail
from .views.suministros import Suministros
from .views.devoluciones import Devoluciones

app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="grass"
    ),
)

