import sys
sys.path.insert(1, 'dsp-modulo')

from thinkdsp import Chirp
from thinkdsp import read_wave

import thinkplot

#signal = Chirp(start = 220, end = 440, amp = 1.0)

#wave = signal.make_wave(duration = 1, framerate = 11025)

wave = read_wave("telefono.wav")
espectro = wave.make_spectrum()
espectrograma = wave.make_spectrogram(seg_length = 1024)


wave.plot()
thinkplot.show()


espectro.plot()
thinkplot.show()

espectrograma.plot()
thinkplot.show()