from pippi import dsp

interval = 1
length = dsp.stf(30)

freq = 100
highfreq = 1000

layers = []
while freq < highfreq:
    layer = dsp.tone(length, freq, amp=0.01)
    layer = dsp.pan(layer, dsp.rand())
    freq += interval

    layers += [ layer ]

out = dsp.mix(layers)

dsp.write(out, 'allfreqs')
