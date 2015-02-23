from pippi import dsp

freq = 440

beat = dsp.mstf(100)
length = dsp.stf(30)
numbeats = length / beat

layers = []

for layer in range(10):
    beats_steady = [ beat for b in range(numbeats / 10) ]
    beats_div = dsp.breakpoint([ dsp.rand(1, 200) for b in range(10) ], numbeats - len(beats_steady))
    ramp = dsp.wavetable('line', len(beats_div))

    beats_div = [ beat + dsp.mstf(d * r) for d, r in zip(beats_div, ramp) ]

    beats = beats_steady + beats_div
    freqs = dsp.wavetable(dsp.randchoose(['line', 'phasor', 'tri', 'hann']), len(beats))
    freqs = [ freq + (100 * f) for f in freqs ]

    layer = ''

    for b, f in zip(beats, freqs):
        blip = dsp.tone(length=b, freq=f, amp=dsp.rand(0.01, 0.2))
        blip = dsp.env(blip, 'phasor')
        blip = dsp.taper(blip, dsp.mstf(5))
        blip = dsp.pan(blip, dsp.rand())

        layer += blip

    layers += [ layer ]

out = dsp.mix(layers)

dsp.write(out, 'blipspray')
