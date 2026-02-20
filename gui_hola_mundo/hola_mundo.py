import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Hola Mundo!")
ventana.geometry("300x100")

# Etiqueta de texto
etiqueta = tk.Label(ventana, text="¡Hola Mundo!", font=("Arial", 14))
etiqueta.pack(pady=20)

# Ejecutar la ventana
ventana.mainloop()
