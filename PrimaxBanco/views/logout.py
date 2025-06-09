import reflex as rx
from ..backend import UserState
from supabase import supabase

@rx.page(route="/logout")
def logout():
    response = supabase.auth.sign_out()
    return rx.center(
        rx.text("Cerrando sesión..."),
        rx.script("window.location.href = '/'")  # Redirige al login
    )