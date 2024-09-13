import tkinter as tk
import random

class JuegoPiedraPapelTijeras(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Piedra, Papel, Tijeras, Lagarto, Spock")
        self.geometry("400x300")

        self.usuario = None
        self.computadora = None

        self.ganadas_computadora = 0
        self.ganadas_usuario = 0
        self.empates = 0

        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        etiqueta_resultado = tk.Label(self, text="Resultado:")
        etiqueta_resultado.pack(pady=10)

        self.etiqueta_ganadas_computadora = tk.Label(self, text="Computadora: 0")
        self.etiqueta_ganadas_computadora.pack()

        self.etiqueta_ganadas_usuario = tk.Label(self, text="Usuario: 0")
        self.etiqueta_ganadas_usuario.pack()

        self.etiqueta_empates = tk.Label(self, text="Empates: 0")
        self.etiqueta_empates.pack()

        opciones = ["Piedra", "Papel", "Tijeras", "Lagarto", "Spock"]

        for opcion in opciones:
            boton = tk.Button(self, text=opcion, command=lambda op=opcion: self.jugar(op))
            boton.pack(side=tk.LEFT, padx=5)

        boton_fin = tk.Button(self, text="Fin de juego", command=self.destroy)
        boton_fin.pack(side=tk.RIGHT, padx=5)

    def jugar(self, opcion_usuario):
        opciones = ["Piedra", "Papel", "Tijeras", "Lagarto", "Spock"]
        self.usuario = opcion_usuario
        self.computadora = random.choice(opciones)

        resultado = self.verificar_ganador()

        self.actualizar_resultados(resultado)

    def verificar_ganador(self):
        reglas = {
            ("Piedra", "Tijeras"): "Piedra aplasta Tijeras",
            ("Tijeras", "Papel"): "Tijeras corta Papel",
            ("Papel", "Piedra"): "Papel envuelve Piedra",
            ("Piedra", "Lagarto"): "Piedra machaca Lagarto",
            ("Lagarto", "Spock"): "Lagarto envenena Spock",
            ("Spock", "Tijeras"): "Spock rompe Tijeras",
            ("Tijeras", "Lagarto"): "Tijeras decapita Lagarto",
            ("Lagarto", "Papel"): "Lagarto se come Papel",
            ("Papel", "Spock"): "Papel desautoriza Spock",
            ("Spock", "Piedra"): "Spock vaporiza Piedra"
        }

        if self.usuario == self.computadora:
            return "Empate"
        elif (self.usuario, self.computadora) in reglas:
            self.ganadas_usuario += 1
            return f"¡Ganaste! {reglas[(self.usuario, self.computadora)]}"
        else:
            self.ganadas_computadora += 1
            return f"Perdiste. {reglas[(self.computadora, self.usuario)]}"

    def actualizar_resultados(self, resultado):
        self.etiqueta_ganadas_computadora.config(text=f"Computadora: {self.ganadas_computadora}")
        self.etiqueta_ganadas_usuario.config(text=f"Usuario: {self.ganadas_usuario}")
        self.etiqueta_empates.config(text=f"Empates: {self.empates}")

        tk.messagebox.showinfo("Resultado", resultado)

if __name__ == "__main__":
    app = JuegoPiedraPapelTijeras()
    app.mainloop()