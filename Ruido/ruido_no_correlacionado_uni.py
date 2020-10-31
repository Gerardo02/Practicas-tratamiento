import sys
sys.path.insert(1, 'dsp-modulo')

import numpy as np
import thinkplot as plt

from thinkdsp import decorate
from thinkdsp import UncorrelatedUniformNoise

signal = UncorrelatedUniformNoise()
wave = signal.make_wave(duration = 0.5, framerate = 22050)
#wave.write("ruido_no_correlacionado_uniforme.wav")

segmento = wave.segment(duration = 0.05)

segmento.plot()
decorate(xlabel = "Tiempo(s)", ylabel = "Amplitud")
plt.show()

espectro = wave.make_spectrum()
espectro.plot_power()
decorate(xlabel = "Frecuencia (Hz)", ylabel = "Poder")
plt.show()

espectro_integrado = espectro.make_integrated_spectrum()
espectro_integrado.plot_power()
decorate(xlabel = "Frecuencia (Hz)", ylabel = "Poder acumulado")
plt.show()

pendiente = espectro.estimate_slope()
print("Pendiente: " + str(pendiente.slope))