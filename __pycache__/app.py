import tkinter as tk
from tkinter import scrolledtext
import json

class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.configure(background="black")
        self.root.iconbitmap("CHATBOT-PYTHON-IA/chatbot.ico")

        # Cargar el archivo JSON
        try:
            with open('CHATBOT-PYTHON-IA\__pycache__\conversaciones.json', 'r') as archivo:
                self.datos = json.load(archivo)
        except FileNotFoundError:
            print("El archivo 'conversaciones.json' no se encontró.")
            self.root.destroy()
            return
        except json.JSONDecodeError:
            print("El archivo 'conversaciones.json' no es válido JSON.")
            self.root.destroy()
            return

        # Configurar el widget de entrada
        self.entrada = tk.Entry(root, width=40)
        self.entrada.pack(pady=10)
        self.entrada.bind("<Return>", self.obtener_respuesta)

        # Configurar el widget de chat
        self.chat = scrolledtext.ScrolledText(root, width=40, height=15)
        self.chat.pack()
        self.chat.config(state=tk.DISABLED)

        # Configurar el botón para enviar la pregunta
        self.boton = tk.Button(root, text="Enviar", background="orange",
                              width=8, height=2, command=self.obtener_respuesta)
        self.boton.pack()

    def obtener_respuesta(self, event=None):
        pregunta = self.entrada.get().lower()
        respuesta = "Lo siento, no entiendo tu pregunta."

        for conversacion in self.datos["conversaciones"]:
            if conversacion["pregunta"].lower() in pregunta:
                respuesta = conversacion["respuesta"]
                break

        self.mostrar_en_chat("Tú: " + pregunta)
        self.mostrar_en_chat("ChatBot: " + respuesta)

    def mostrar_en_chat(self, mensaje):
        self.chat.config(state=tk.NORMAL)
        self.chat.insert(tk.END, mensaje + "\n")
        self.chat.config(state=tk.DISABLED)
        self.entrada.delete(0, tk.END)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = ChatBotApp(ventana)
    ventana.mainloop()

