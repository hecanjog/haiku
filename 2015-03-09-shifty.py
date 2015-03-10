from pippi import dsp
from hcj import data

numgrains = 1000
numsines = 100
length = dsp.mstf(100)

dist = data.Logistic(3.99, 0.5, numsines).data
dist = sorted(dist)

lows = dsp.breakpoint([ dsp.rand(10, 100) for _ in range(100) ], numgrains)
highs = dsp.breakpoint([ dsp.rand(100, 1000) for _ in range(100) ], numgrains)

out = ''
for lowfreq, highfreq in zip(lows, highs):
    layers = []

    for freq in dist:
        r = highfreq - lowfreq
        layers += [ dsp.pan(dsp.tone(length, freq * r + lowfreq, amp=0.05), dsp.rand()) ]

    out += dsp.taper(dsp.env(dsp.mix(layers), 'hann'), dsp.mstf(10))

dsp.write(out, 'shifty')
