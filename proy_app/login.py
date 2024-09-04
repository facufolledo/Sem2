import reflex as rx
from .funciones import verificar_credenciales

class LoginState(rx.State):
    username: str = ""
    password: str = ""
    error_message: str = ""

    def verificar(self):
        if verificar_credenciales(self.username, self.password):
            return rx.redirect("/home")
        else:
            self.error_message = "Error de inicio de sesión. Verifique su usuario y contraseña."

@rx.page(route="/login", title="Inicio de Sesión")
def login() -> rx.Component:
    return rx.section(
        rx.flex(
            rx.heading("Inicio de Sesión"),
            rx.text("Ingrese su nombre de usuario"),
            rx.input(placeholder="Nombre de usuario", on_change=LoginState.set_username),
            rx.text("Ingrese su contraseña"),
            rx.input(type="password", placeholder="Contraseña", on_change=LoginState.set_password),
            rx.button("Iniciar Sesión", type="submit", on_click=LoginState.verificar),
            direction="column",
            gap="1rem",
        ),
        padding="2rem",
        width="100%",
        align_items="center",
    )
