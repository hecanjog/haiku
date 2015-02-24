from pippi import dsp
from pippi import tune
from hcj import keys

chords = tune.chords(['i', 'vi9', 'iii7', 'v'], 'a', octave=3, ratios=tune.terry)

out = ''

for chord in chords * 4:
    layers = []
    length = dsp.stf(dsp.rand(3,4))
    for freq in chord:
        layer = keys.rhodes(length, freq, dsp.rand(0.1, 0.2))
        layer = dsp.pan(layer, dsp.rand())
        layer = dsp.drift(layer, dsp.rand(0, 0.01))

        layers += [ layer ]

    chord = dsp.mix(layers)
    chord = dsp.drift(chord, dsp.rand(0, 0.01))

    out += chord

dsp.write(out, 'chordsweep')
