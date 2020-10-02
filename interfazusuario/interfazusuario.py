from tkinter import *

ventana = Tk()
ventana.title("La ventana")
ventana.geometry("800x600")

etiqueta = Label(ventana, text = "Esto es una etiqueta")
etiqueta.pack()

etiqueta2 = Label(ventana, text = "Esto es otra etiqueta")
etiqueta2.pack()

ingresoTexto = Entry(ventana)
ingresoTexto.pack()


boton = Button(ventana, text = "El boton")
boton.pack()

ventana.mainloop()