import sys 
sys.path.insert(1,'dsp-modulo')

from tkinter import *
from tkinter.filedialog import askopenfilename

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from thinkdsp import read_wave
import numpy

principal = Tk()
principal.title("Analisis audio")


strDireccionArchivo = StringVar()
strDireccionArchivo.set("Direccion del archivo:")

strSecuencia = StringVar()
strSecuencia.set("Numero de contenido en el audio:")

def abrirArchivo():
    direccionArchivo = askopenfilename()
    strDireccionArchivo.set("Direccion del archivo: " + direccionArchivo)


    telefono = ""
    waveTelefono = read_wave(direccionArchivo)

    segmentosNumeros = []

    
    for i in range(6):
        segmentosNumeros.append(waveTelefono.segment(start=i*0.5, duration=0.5))


    frecuenciasBajasDTMF = [697, 770, 852, 941]
    frecuenciasAltasDTMF = [1209, 1336, 1477]
    tolerancia = 10

    for segmento in segmentosNumeros:
        espectroSegmento = segmento.make_spectrum()
        frecuenciasDominantes = []
        i = 0
        for amplitudEspectral in espectroSegmento.hs:
            if numpy.abs(amplitudEspectral) > 500:
                frecuenciasDominantes.append(espectroSegmento.fs[i])
            i = i + 1
        frecuenciaBaja = 0
        frecuenciaAlta = 0
        for frecuencia in frecuenciasDominantes:
            for frecuenciaDTMF in frecuenciasBajasDTMF:
                if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                    frecuenciaBaja = frecuenciaDTMF
            for frecuenciaDTMF in frecuenciasAltasDTMF:
                if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                    frecuenciaAlta = frecuenciaDTMF
        if frecuenciaAlta == 1209:
            if frecuenciaBaja == 697:
                telefono = telefono + "1"
            elif frecuenciaBaja == 770:
                telefono = telefono + "4"
            elif frecuenciaBaja == 852:
                telefono = telefono + "7"
            elif frecuenciaBaja == 941:
                telefono = telefono + "*"
            else:
                telefono = telefono + "X"
        elif frecuenciaAlta == 1336:
            if frecuenciaBaja == 697:
                telefono = telefono + "2"
            elif frecuenciaBaja == 770:
                telefono = telefono + "5"
            elif frecuenciaBaja == 852:
                telefono = telefono + "8"
            elif frecuenciaBaja == 941:
                telefono = telefono + "0"
            else:
                telefono = telefono + "X"
        elif frecuenciaAlta == 1477:
            if frecuenciaBaja == 697:
                telefono = telefono + "3"
            elif frecuenciaBaja == 770:
                telefono = telefono + "6"
            elif frecuenciaBaja == 852:
                telefono = telefono + "9"
            elif frecuenciaBaja == 941:
                telefono = telefono + "#"
            else:
                telefono = telefono + "X"
        else:
            telefono = telefono + "X"

    


    strSecuencia.set("Numero de contenido en el audio: " + telefono)

    figure = Figure(figsize = (5,3), dpi = 100)
    figure.add_subplot(111).plot(waveTelefono.ts, waveTelefono.ys)
    canvas = FigureCanvasTkAgg(figure, master = principal)
    canvas.draw()
    canvas.get_tk_widget().pack()




btnAbrir = Button(principal, text = "Abriri archivo wav", command = abrirArchivo)
btnAbrir.pack()

lblArchivo = Label(principal, textvariable = strDireccionArchivo)
lblArchivo.pack()

lblSecuenciaNumeros = Label(principal, textvariable = strSecuencia)
lblSecuenciaNumeros.pack()

mainloop()