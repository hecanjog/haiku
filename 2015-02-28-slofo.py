from pippi import dsp
from pippi import tune

chord = tune.chord('I', octave=2, ratios=tune.terry)

length = dsp.stf(120)

layers = []
for freq in chord:
    takes = []
    for take in range(4):
        lfos = []
        for lfo in range(3):
            lf = dsp.rand(0.01, 0.1)
            lwf = dsp.breakpoint([0] + [ dsp.rand(0, 1) for p in range(5) ] + [0], 512)
            lfo = dsp.ctone(lf, length, lwf, dsp.rand(0.75, 1))
            lfos += [ lfo ]

        wf = dsp.wavetable('tri', 512)
        amp = 0.5

        take = dsp.ctone(freq, length, wf, amp)
        for lfo in lfos:
            take = dsp.am(take, lfo)

        takes += [ dsp.pan(take, dsp.rand()) ]

    layers += [ dsp.mix(takes) ]

out = dsp.mix(layers)

dsp.write(out, 'slofo')
