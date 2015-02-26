from pippi import dsp

freqs = [55, 220, 440, 770]
length = dsp.stf(90)

layers = []

for freq in freqs:
    amp = dsp.rand(0.05, 0.1)

    wf1 = dsp.breakpoint([ dsp.rand(-1, 1) for p in range(7) ], 512)
    wf2 = dsp.breakpoint([ dsp.rand(-1, 1) for p in range(4) ], 512)

    layer = dsp.subtract(dsp.ctone(freq * 0.999, length, wf1, amp), dsp.ctone(freq, length, wf2, amp))
    layer = dsp.pan(layer, dsp.rand())
    layer = dsp.env(layer, 'random')

    layers += [ layer ]

out = dsp.mix(layers)

dsp.write(out, 'retabler')
