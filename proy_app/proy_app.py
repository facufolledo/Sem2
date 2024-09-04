import reflex as rx
from .funciones import test_connection

def index():
    # Verificar conexión y mostrar mensaje
    connection_status = test_connection()

    return rx.text("Estado de la conexión: " + connection_status)

app = rx.App()
app.add_page(index)

if __name__ == "__main__":
    app.run()

