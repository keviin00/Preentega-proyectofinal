# Diccionario para almacenar información de usuario y contraseña
usuarios = {}

# Función para registrar un usuario
def registrar_usuario(usuario, contraseña):
    if usuario not in usuarios:
        usuarios[usuario] = contraseña
        print("Registro exitoso.")
    else:
        print("El usuario ya existe.")

# Función para mostrar la información de usuarios registrados
def mostrar_usuarios():
    print("Usuarios registrados:")
    for usuario in usuarios:
        print(usuario)

# Función para realizar el inicio de sesión
def iniciar_sesion(usuario, contraseña):
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Inicio de sesión exitoso.",usuario)
    else:
        print("Credenciales incorrectas.")

# Función principal del programa
def main():
    while True:
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Iniciar sesión")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario = input("Ingresa el nombre de usuario: ")
            contraseña = input("Ingresa la contraseña: ")
            registrar_usuario(usuario, contraseña)
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            usuario = input("Ingresa el nombre de usuario: ")
            contraseña = input("Ingresa la contraseña: ")
            iniciar_sesion(usuario, contraseña)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()


