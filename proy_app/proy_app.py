import reflex as rx
from .funciones import test_connection

@rx.page(route="/", title="Inicio")
def index() -> rx.Component:
    connection_status = test_connection()
    
    if connection_status == "Conexión exitosa":
        return rx.section(
            rx.flex(
                rx.heading("Bienvenido"),
                rx.text("La conexión a la base de datos joyaaa."),
                rx.button("Entrar", on_click=lambda: rx.redirect("/login")),
                direction="column",
                gap="1rem",
            ),
            padding="2rem",
            width="100%",
            align_items="center",
        )
    else:
        return rx.section(
            rx.text("Error: " + connection_status),
            padding="2rem",
            width="100%",
            align_items="center",
        )

app = rx.App()
app.add_page(index)

if __name__ == "__main__":
    app.run()
