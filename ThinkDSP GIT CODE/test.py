import numpy as np
import matplotlib.pyplot as plt

from thinkdsp import decorate

from thinkdsp import Chirp

signal = Chirp(start=220, end=880)
wave1 = signal.make_wave(duration=2)
print(wave)
wave1.make_audio()