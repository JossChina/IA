import tkinter as tk
import random

# Definir las opciones del juego
opciones = ["Piedra", "Papel", "Tijeras", "Lagarto", "Spock"]

# Inicializar contadores
victorias_computadora = 0
victorias_usuario = 0
empates = 0

# Función para la lógica del juego
def jugar(opcion_usuario):
    global victorias_computadora, victorias_usuario, empates

    # Elección aleatoria de la computadora
    opcion_computadora = random.choice(opciones)

    # Lógica del juego mejorado
    reglas = {
        "Piedra": ["Tijeras", "Lagarto"],
        "Papel": ["Piedra", "Spock"],
        "Tijeras": ["Papel", "Lagarto"],
        "Lagarto": ["Papel", "Spock"],
        "Spock": ["Tijeras", "Piedra"]
    }

    if opcion_usuario == opcion_computadora:
        resultado = "Empate"
        empates += 1
    elif opcion_computadora in reglas[opcion_usuario]:
        resultado = "¡Ganaste!"
        victorias_usuario += 1
    else:
        resultado = "¡La computadora ganó!"
        victorias_computadora += 1

    # Actualizar etiquetas en la interfaz gráfica
    label_computadora.config(text=f"Computadora: {opcion_computadora}")
    label_usuario.config(text=f"Tú: {opcion_usuario}")
    label_resultado.config(text=resultado)
    label_estadisticas.config(text=f"Victorias: {victorias_usuario} | Derrotas: {victorias_computadora} | Empates: {empates}")

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Piedra, Papel, Tijeras, Lagarto, Spock")

# Etiquetas
label_computadora = tk.Label(ventana, text="Computadora: ")
label_usuario = tk.Label(ventana, text="Tú: ")
label_resultado = tk.Label(ventana, text="")
label_estadisticas = tk.Label(ventana, text="Victorias: 0 | Derrotas: 0 | Empates: 0")

# Botones
for opcion in opciones:
    tk.Button(ventana, text=opcion, command=lambda op=opcion: jugar(op)).pack()

# Mostrar etiquetas
label_computadora.pack()
label_usuario.pack()
label_resultado.pack()
label_estadisticas.pack()

# Ejecutar la aplicación
ventana.mainloop()