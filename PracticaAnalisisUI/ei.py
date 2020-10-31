import sys 
sys.path.insert(1, 'dsp-modulo')

from tkinter import *
from tkinter.filedialog import askopenfilename

from thinkdsp import read_wave
import numpy

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

principal = Tk()
principal.title("Analisis audio")

direccionlbl = StringVar()
direccionlbl.set("Direccion del archivo:")

strDireccionArchivo = StringVar()
strDireccionArchivo.set("")

mensajelbl = StringVar()
mensajelbl.set("Mensaje cifrado:")

strSecuencia = StringVar()
strSecuencia.set("")

direccionArchivo = ""

def abrirArchivo():
    global direccionArchivo
    direccionArchivo = askopenfilename()
    strDireccionArchivo.set(direccionArchivo)

def analizar():
    global direccionArchivo
    audio = ""
    waveAudio = read_wave(direccionArchivo)
    #Tamaño del segmento
    sizeSegmento = 0

    primerSegmento = []
    primerSegmento.append(waveAudio.segment(start=0, duration=0.4))

    frecuenciaSegmento = [1000, 600, 400]
    tolerancia = 10

    for segmento in primerSegmento:
        espectroSegmento = segmento.make_spectrum()
        frecuenciasDominantes = []
        i = 0
        for amplitudEspectral in espectroSegmento.hs:
            if numpy.abs(amplitudEspectral) > 500:
                frecuenciasDominantes.append(espectroSegmento.fs[i])
            i = i + 1
        sizeSegmentoFrecuencia = 0
        for frecuencia in frecuenciasDominantes:
            for frecuenciaDTMF in frecuenciaSegmento:
                if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                    sizeSegmentoFrecuencia = frecuenciaDTMF

                    
        if sizeSegmentoFrecuencia == 1000:
            sizeSegmento = 0.3
        elif sizeSegmentoFrecuencia == 600:
            sizeSegmento = 0.4
        elif sizeSegmentoFrecuencia == 400:
            sizeSegmento = 0.5


    #Cantidad de letras
    cantidadLetras = 0

    segundoSegmento = []
    segundoSegmento.append(waveAudio.segment(start=0.4, duration=0.4))

    frecuenciaCantidadLetras = [200, 450, 700, 950, 1200, 1450, 1700]

    for segmento in segundoSegmento:
        espectroSegmento = segmento.make_spectrum()
        frecuenciasDominantes = []
        i = 0
        for amplitudEspectral in espectroSegmento.hs:
            if numpy.abs(amplitudEspectral) > 500:
                frecuenciasDominantes.append(espectroSegmento.fs[i])
            i = i + 1
        cantidadLetrasFrecuencia = 0
        for frecuencia in frecuenciasDominantes:
            for frecuenciaDTMF in frecuenciaCantidadLetras:
                if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                    cantidadLetrasFrecuencia = frecuenciaDTMF
        if cantidadLetrasFrecuencia == 200:
            cantidadLetras = 2
        elif cantidadLetrasFrecuencia == 450:
            cantidadLetras = 3
        elif cantidadLetrasFrecuencia == 700:
            cantidadLetras = 4
        elif cantidadLetrasFrecuencia == 950:
            cantidadLetras = 5
        elif cantidadLetrasFrecuencia == 1200:
            cantidadLetras = 6
        elif cantidadLetrasFrecuencia == 1450:
            cantidadLetras = 7
        elif cantidadLetrasFrecuencia == 1700:
            cantidadLetras = 8

    #Letras
    letrasSegmento = []
    for i in range(cantidadLetras):
        letrasSegmento.append(waveAudio.segment(start=0.8+i*sizeSegmento, duration=sizeSegmento))

    frecuenciaLetras = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700]

    for segmento in letrasSegmento:
        espectroSegmento = segmento.make_spectrum()
        frecuenciasDominantes = []
        i = 0
        for amplitudEspectral in espectroSegmento.hs:
            if numpy.abs(amplitudEspectral) > 500:
                frecuenciasDominantes.append(espectroSegmento.fs[i])
            i = i + 1
        LetrasFrecuencia = 0
        for frecuencia in frecuenciasDominantes:
            for frecuenciaDTMF in frecuenciaLetras:
                if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                    LetrasFrecuencia = frecuenciaDTMF
        if LetrasFrecuencia == 200:
            audio = audio + "A"
        elif LetrasFrecuencia == 300:
            audio = audio + "B"
        elif LetrasFrecuencia == 400:
            audio = audio + "C"
        elif LetrasFrecuencia == 500:
            audio = audio + "D"
        elif LetrasFrecuencia == 600:
            audio = audio + "E"
        elif LetrasFrecuencia == 700:
            audio = audio + "F"
        elif LetrasFrecuencia == 800:
            audio = audio + "G"
        elif LetrasFrecuencia == 900:
            audio = audio + "H"
        elif LetrasFrecuencia == 1000:
            audio = audio + "I"
        elif LetrasFrecuencia == 1100:
            audio = audio + "J"
        elif LetrasFrecuencia == 1200:
            audio = audio + "K"
        elif LetrasFrecuencia == 1300:
            audio = audio + "L"
        elif LetrasFrecuencia == 1400:
            audio = audio + "M"
        elif LetrasFrecuencia == 1500:
            audio = audio + "N"
        elif LetrasFrecuencia == 1600:
            audio = audio + "O"
        elif LetrasFrecuencia == 1700:
            audio = audio + "P"
        elif LetrasFrecuencia == 1800:
            audio = audio + "Q"
        elif LetrasFrecuencia == 1900:
            audio = audio + "R"
        elif LetrasFrecuencia == 2000:
            audio = audio + "S"
        elif LetrasFrecuencia == 2100:
            audio = audio + "T"
        elif LetrasFrecuencia == 2200:
            audio = audio + "U"
        elif LetrasFrecuencia == 2300:
            audio = audio + "V"
        elif LetrasFrecuencia == 2400:
            audio = audio + "W"
        elif LetrasFrecuencia == 2500:
            audio = audio + "X"
        elif LetrasFrecuencia == 2600:
            audio = audio + "Y"
        elif LetrasFrecuencia == 2700:
            audio = audio + "Z"

    strSecuencia.set(audio)

    #figure = Figure(figsize=(5,3), dpi=100)
    #figure.add_subplot(111).plot(waveAudio.ts, waveAudio.ys)
    #canvas = FigureCanvasTkAgg(figure, master=principal)
    #canvas.draw()
    #canvas.get_tk_widget().pack()

btnAbrir = Button(principal, text="Abrir archivo wav", command=abrirArchivo)
btnAbrir.pack()

btnAnalizar = Button(principal, text="Analizar", command=analizar)
btnAnalizar.pack()

lblArchivo = Label(principal, textvariable=direccionlbl)
lblArchivo.pack()

lblArchivo = Label(principal, textvariable=strDireccionArchivo)
lblArchivo.pack()

lblArchivo = Label(principal, textvariable=mensajelbl)
lblArchivo.pack()

lblSecuenciaNumeros = Label(principal, textvariable=strSecuencia)
lblSecuenciaNumeros.pack()

mainloop()