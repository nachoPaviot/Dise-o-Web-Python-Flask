from app import app

# Si ejecutamos el módulo, la aplicación de Flask corre con el modo de prueba
# activo.
if __name__ == "__main__":
    app.run(debug=False)