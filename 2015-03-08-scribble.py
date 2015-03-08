from pippi import dsp
from hcj import data

def chirp():
    r = dsp.rand(3.6, 3.99)
    numpoints = dsp.randint(10, 30)

    freq = dsp.rand(200, 1000)
    slength = dsp.rand(0.05, 0.5)
    length = dsp.stf(slength)

    log = data.Logistic(r, size=numpoints)
    mod = dsp.breakpoint([0] + [ dsp.rand() for r in range(numpoints / 3) ] + [0], numpoints)
    mod = [ p * log.get() for p in mod ]
    modr = dsp.rand(1, 5)
    modf = 1.0 / slength

    wf = dsp.wavetable('sine2pi', 512)
    win = dsp.wavetable('sine', 512)
    pw = dsp.rand(0.5, 1)
    amp = dsp.rand(0.1, 0.3)

    out = dsp.pulsar(freq, length, pw, wf, win, mod, modr, modf, amp)
    out = dsp.env(out, 'random')
    out = dsp.taper(out, dsp.mstf(10))
    out = dsp.pan(out, dsp.rand())
    out = dsp.pad(out, 0, dsp.stf(dsp.rand(0.1, 0.3)))

    return out

out = ''.join([ dsp.mix([ chirp() for c in range(dsp.randint(2, 10)) ]) for o in range(100) ])

dsp.write(out, 'scribble')
