from pippi import dsp
from pippi import tune

length = dsp.stf(45)

freqs = [ dsp.rand(20, 200) for f in range(10) ]

def makeLayer(freq):
    pw = dsp.rand()
    wf = dsp.wavetable('tri', 512)
    win = dsp.wavetable('hann', 512)
    mod = dsp.breakpoint([ dsp.rand() for m in range(dsp.randint(4,8)) ], 512)
    modf = dsp.rand(0.1, 2)
    modr = dsp.rand(0, 0.01)
    amp = dsp.rand(0.1, 0.5)

    layer = dsp.pulsar(freq, length, pw, wf, win, mod, modf, modr, amp)

    return layer

layers = [ makeLayer(freq) for freq in freqs ]

out = dsp.mix(layers)

dsp.write(out, 'fuzzlo')
