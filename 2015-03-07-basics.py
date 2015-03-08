from pippi import dsp

dist = dsp.wavetable('hann', 1200)[:600]

lowfreq = 200
highfreq = 1000
length = dsp.stf(60)

layers = []

for freq in dist:
    r = highfreq - lowfreq
    layers += [ dsp.tone(length, freq * r + lowfreq, amp=0.01) ]

out = dsp.mix(layers)

dsp.write(out, 'basics')
