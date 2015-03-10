from pippi import dsp
from hcj import data

numevents = 100
numlayers = 3

layers = []

for _ in range(numlayers):
    layer = ''

    for _ in range(numevents):
        slength = dsp.rand(0.1, 4)
        length = dsp.stf(slength)
        freq = (1.0 / slength) * dsp.rand(0.5, 10)
        amp = dsp.rand(0.1, 0.5)

        log = dsp.breakpoint(data.Logistic(dsp.rand(3.88, 3.99), 0.5, length / 10).data, length)
        mult = dsp.breakpoint([0] + [ dsp.rand(-1, 1) for _ in range(dsp.randint(50, 100)) ] + [0], length)

        wf = [ m * l for m, l in zip(mult, log) ]

        o = dsp.ctone(freq, length, wf, amp)
        o = dsp.env(o, 'random')
        o = dsp.pan(o, dsp.rand())
        o = dsp.taper(o, dsp.mstf(20))

        layer += o

    layers += [ layer ]

out = dsp.mix(layers)

dsp.write(out, 'lipsys')
