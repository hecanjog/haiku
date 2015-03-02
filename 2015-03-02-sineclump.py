from pippi import dsp

length = dsp.stf(30)

freq = 100
highfreq = 200

count = 0
layers = []
while freq < highfreq:
    layer = dsp.tone(length, freq, amp=0.001)
    layer = dsp.pan(layer, dsp.rand())
    freq += dsp.rand(0.05, 0.1)

    layers += [ layer ]
    count += 1

print count
out = dsp.mix(layers)

dsp.write(out, 'sineclump')
