from tkinter import *

ventana = Tk()
ventana.title("La calculadora de las propinas")
ventana.geometry("400x400")

strTotal = StringVar()
strTotal.set("$0.0")

def calcular():
    total = float(txtCuenta.get()) + float(txtCuenta.get()) * (float(sclPropina.get()) / 100.0)
    strTotal.set("$" + str(total))

lblCuenta = Label(ventana, text = "Cuenta:")
lblCuenta.pack()

txtCuenta = Entry(ventana)
txtCuenta.pack()

lblPorcentajePropina = Label(ventana, text = "Porcentaje de propina:")
lblPorcentajePropina.pack()

sclPropina = Scale(ventana, from_ = 0, to_ = 20, orient = HORIZONTAL)
sclPropina.pack()

btnCalcular = Button(ventana, text = "Calcular", command = calcular)
btnCalcular.pack()

lblTotalAPagar = Label(ventana, text = "Total a pagar:")
lblTotalAPagar.pack()

lblMontoTotal = Label(ventana, textvariable = strTotal)
lblMontoTotal.pack()

ventana.mainloop()