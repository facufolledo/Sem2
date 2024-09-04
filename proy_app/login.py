import reflex as rx
import requests as rq

@rx.page(route="/login", title="Inicio de Sesión")
def login() -> rx.Component:
    """Retorna el componente de la página de inicio de sesión."""
    return rx.section(
        rx.flex(
            rx.heading("Inicio de Sesión"),
            rx.text("Ingrese su nombre de usuario"),
            rx.input(placeholder="Nombre de usuario"),  # Campo de texto para el nombre de usuario
            rx.text("Ingrese su contraseña"),
            rx.input(type="password", placeholder="Contraseña"),  # Campo de texto para la contraseña
            rx.button("Iniciar Sesión", type="submit"),  # Botón de inicio de sesión
            direction="column",  # Alineación vertical de los elementos
            gap="1rem",  # Espacio entre los elementos
        ),
        padding="2rem",  # Relleno alrededor del formulario
        width="100%",  # Ancho del contenedor
        align_items="center",  # Alinear los elementos al centro
    )
