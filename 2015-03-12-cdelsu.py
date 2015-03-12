from pippi import dsp
from hcj import data

layers = []

numgrains = 55555

for _ in range(4):
    layer = ''

    pans = dsp.breakpoint([ dsp.rand() for _ in range(55) ], numgrains)
    lens = [ dsp.mstf(l * 80 + 20) for l in dsp.wavetable('line', numgrains / dsp.randint(50, 100)) ]
    seeds = [ s * 0.3 + 3.69 for s in dsp.wavetable('line', numgrains / dsp.randint(50, 100)) ]
    freqs = [ f * 90 + 10 for f in dsp.wavetable('line', numgrains / dsp.randint(50, 100)) ]

    for freq, seed, length, pan in zip(freqs, seeds, lens, pans):
        log = data.Logistic(seed, 0.5, 555)
        amp = dsp.rand(0.1, 0.75)

        grain = dsp.ctone(freq, length, log.data, amp)
        grain = dsp.env(grain, 'random')
        grain = dsp.taper(grain, dsp.mstf(5))
        grain = dsp.pan(grain, pan)

        layer += grain

    layers += [ layer ]

out = dsp.mix(layers)

dsp.write(out, 'cdelsu')
