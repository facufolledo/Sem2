import reflex as rx
import requests as rq

@rx.page(route="/login", title="Login")
def login() -> rx.Component:
    """Returns the login page component."""
    return rx.section(
        rx.flex(
            rx.image(
                src="/login.jpg",
                width="300px",
                borderRadius="15px 50px"
            ),
            rx.heading("Login"),
        )
    )
