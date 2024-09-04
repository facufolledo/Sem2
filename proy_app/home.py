import reflex as rx

@rx.page(route="/home", title="Página de Inicio")
def home() -> rx.Component:
    return rx.section(
        rx.flex(
            rx.heading("Bienvenido!"),
            rx.text("Usuario correcto."),
            direction="column",
            gap="1rem",
        ),
        padding="2rem",
        width="100%",
        align_items="center",
    )
