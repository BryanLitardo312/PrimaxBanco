import reflex as rx

from .components.stats_cards import stats_cards_group
from .views.navbar import navbar
from .views.table import main_table
from .views.login import login
from .views.novedades import Novedades
from .views.detalle import detalle

app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="grass"
    ),
)

