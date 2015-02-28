from pippi import dsp
from pippi import tune

chord = tune.chord('I', octave=2, ratios=tune.terry)

length = dsp.stf(120)

layers = []
for freq in chord:
    lfos = []
    for lfo in range(6):
        lf = dsp.rand(0.1, 1)
        lwf = dsp.breakpoint([ dsp.rand(0, 1) for p in range(5) ], 512)
        lfo = dsp.ctone(lf, length, lwf, dsp.rand(0.75, 1))
        lfos += [ lfo ]

    lfo = dsp.mix(lfos)

    wf = dsp.wavetable('tri', 512)
    amp = 0.2

    layer = dsp.ctone(freq, length, wf, amp)
    layer = dsp.mul(layer, lfo)

    layers += [ layer ]

out = dsp.mix(layers)

dsp.write(out, 'slofo')
