from pippi import dsp
from pippi import tune

chord = tune.chord('I', octave=2, key='a', ratios=tune.terry)

numsegs = 2222
length = dsp.stf(60) / numsegs
numpoints = 7

wfs = [ dsp.breakpoint([ dsp.rand(-1, 1) for p in range(numpoints) ], 512) for _ in range(numsegs) ]
win = dsp.wavetable('tri', 512)

mods = [ dsp.breakpoint([ dsp.rand(0, 1) for p in range(numpoints) ], 512) for _ in range(numsegs) ]
modfs = [ dsp.rand(0.01, 0.1) for _ in range(numsegs) ]
modrs = [ dsp.rand(0, 0.1) for _ in range(numsegs) ]
pws = [ dsp.rand(0.01, 1) for _ in range(numsegs) ]

out = []

for wf, mod, modf, modr, pw in zip(wfs, mods, modfs, modrs, pws):
    layers = []
    for freq in chord:
        layer = dsp.pulsar(freq, length, pw, wf, win, mod, modr, modf, 0.1)
        layers += [ layer ]

    out += [ dsp.mix(layers) ]

out = [ dsp.taper(o, dsp.mstf(10)) for o in out ]
out = ''.join(out)

dsp.write(out, 'truckidle')
