from pippi import dsp
from hcj import data

layers = []

numgrains = 5555

for _ in range(2):
    layer = ''
    pans = dsp.breakpoint([ dsp.rand() for _ in range(55) ], numgrains)

    for i in range(numgrains):
        freq = dsp.rand(10, 100)
        log = data.Logistic(dsp.rand(3.78, 3.99), 0.5, 555)
        amp = dsp.rand(0.1, 0.5)

        grain = dsp.ctone(freq, dsp.mstf(dsp.rand(5, 150)), log.data, amp)
        grain = dsp.env(grain, 'random')
        grain = dsp.taper(grain, dsp.mstf(5))
        grain = dsp.pan(grain, pans[i])

        layer += grain

    layers += [ layer ]

out = dsp.mix(layers)

dsp.write(out, 'cludes')
