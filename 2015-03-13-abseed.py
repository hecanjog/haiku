from pippi import dsp
from hcj import data

out = ''
tlength = dsp.stf(120)
elapsed = 0
seed = 3.8

while elapsed < tlength:
    layers = []

    for _ in range(4):
        layer = ''
        numgrains = dsp.randint(55, 555)

        pans = dsp.breakpoint([ dsp.rand() for _ in range(55) ], numgrains)
        lens = [ dsp.mstf(l * 80 + 20) for l in dsp.wavetable('line', numgrains / dsp.randint(50, 100)) ]
        freqs = [ f * 90 + 10 for f in dsp.wavetable('line', numgrains / dsp.randint(50, 100)) ]

        for freq, length, pan in zip(freqs, lens, pans):
            seed += 0.00001
            log = data.Logistic(seed, 0.5, 555)
            amp = dsp.rand(0.1, 0.75)

            grain = dsp.ctone(freq, length, log.data, amp)
            grain = dsp.env(grain, 'random')
            grain = dsp.taper(grain, dsp.mstf(5))
            grain = dsp.pan(grain, pan)

            layer += grain

        layers += [ layer ]

    stream = dsp.mix(layers)
    stream = dsp.env(stream, 'random')

    elapsed += dsp.flen(stream)

    out += stream

print seed

dsp.write(out, 'abseed')
