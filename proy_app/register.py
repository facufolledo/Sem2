import reflex as rx
from .funciones import verificar_credenciales, registrar_usuario  # Asegúrate de tener una función para registrar usuarios

class RegisterState(rx.State):
    username: str = ""
    email: str = ""
    dni: str = ""
    password: str = ""
    confirm_password: str = ""
    error_message: str = ""

    def registrar(self):
        if self.password != self.confirm_password:
            self.error_message = "Las contraseñas no coinciden."
            return
        
        if registrar_usuario(self.username, self.email, self.dni, self.password):  # Verifica que la función para registrar usuarios esté definida
            return rx.redirect("/login")
        else:
            self.error_message = "Error al registrarse. Por favor, inténtelo de nuevo."

app = rx.App()

@rx.page(route="/register", title="Registro")
def register() -> rx.Component:
    return rx.box(
        # Contenedor exterior principal
        rx.box(
            # Título
            rx.text("Bienvenido!", font_size="2.8rem", font_weight="bold", color="#333", mt="1.5rem"),
            rx.spacer(1),
            # Cuadro de registro
          
            rx.box(
                
                rx.text("Nombre de usuario", color="#333", font_size="0.9rem"),
                rx.input(
                    placeholder="Nombre de usuario",
                    on_change=RegisterState.set_username,
                    padding="0.5rem",
                    border_radius="0.3rem",
                    border="1px solid #ccc",
                    focus_border_color="#333",
                    background_color="#f9f9f9",
                    style={"color": "#000"}
                ),
                rx.text("Correo electrónico", color="#333", font_size="0.9rem", mt="0.5rem"),
                rx.input(
                    placeholder="Correo electrónico",
                    on_change=RegisterState.set_email,
                    padding="0.5rem",
                    border_radius="0.3rem",
                    border="1px solid #ccc",
                    focus_border_color="#333",
                    background_color="#f9f9f9",
                    style={"color": "#000"}
                ),
                rx.text("DNI", color="#333", font_size="0.9rem", mt="0.5rem"),
                rx.input(
                    placeholder="DNI",
                    on_change=RegisterState.set_dni,
                    padding="0.5rem",
                    border_radius="0.3rem",
                    border="1px solid #ccc",
                    focus_border_color="#333",
                    background_color="#f9f9f9",
                    style={"color": "#000"}
                ),
                rx.text("Contraseña", color="#333", font_size="0.9rem", mt="0.5rem"),
                rx.input(
                    type="password",
                    placeholder="Contraseña",
                    on_change=RegisterState.set_password,
                    padding="0.5rem",
                    border_radius="0.3rem",
                    border="1px solid #ccc",
                    focus_border_color="#333",
                    background_color="#f9f9f9",
                    style={"color": "#000"}
                ),
                rx.text("Confirmar Contraseña", color="#333", font_size="0.9rem", mt="0.5rem"),
                rx.input(
                    type="password",
                    placeholder="Confirmar Contraseña",
                    on_change=RegisterState.set_confirm_password,
                    padding="0.5rem",
                    border_radius="0.3rem",
                    border="1px solid #ccc",
                    focus_border_color="#333",
                    background_color="#f9f9f9",
                    style={"color": "#000"}
                ),
                rx.spacer(1),
                rx.button(
                    "Registrar",
                    type="submit",
                    on_click=RegisterState.registrar,
                    bg="#333",
                    color="white",
                    width="100%",
                    padding="0.5rem",
                    border_radius="0.3rem",
                    mt="1rem",
                    _hover={"bg": "#555"},
                    box_shadow="0 6px 12px rgba(0, 0, 0, 0.3)",
                ),
                # Mensaje de error
                rx.cond(RegisterState.error_message != "", 
                        rx.text(RegisterState.error_message, color="red", mt="0.5rem")),
                padding="1.5rem",
                border="1px solid rgba(128, 128, 128, 0.5)",
                border_radius="0.5rem",
                width="22rem",
                box_shadow="0 12px 24px rgba(0, 0, 0, 0.2)",
                bg="rgba(255, 255, 255, 0.3)",
                mt="1.5rem",
                margin="auto",
            ),
            direction="column",
            align_items="center",
            justify_content="center",
            gap="1.5rem",
            text_align="center",
            border="1px solid rgba(128, 128, 128, 0.3)",
            border_radius="0.5rem",
            bg="rgba(128, 128, 128, 0.1)",
            width="30rem",
            padding="2rem",
        ),
        height="100vh",
        justify_content="center",
        align_items="center",
        display="flex",
        bg="#F5F5DC",
    )


