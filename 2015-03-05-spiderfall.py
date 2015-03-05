from pippi import dsp

g = dsp.read('sounds/seneca3bars.wav').data

numsections = 12
numlayers = 30
numgrains = 22

sections = []
for s in range(numsections):
    layers = []

    for layer in range(numlayers):
        minlen = 40
        lenrange = dsp.rand(300, 500)
        lengths = dsp.wavetable('hann', numgrains * 2)[:numgrains]
        lengths = [ dsp.mstf(l * lenrange + minlen) for l in lengths ]
        pans = dsp.breakpoint([ dsp.rand() for p in range(numgrains / 3)], numgrains)

        layers += [ (lengths, pans) ]

    sections += [ layers ]

out = ''
for section in sections:
    layers = []
    for layer in section:
        startpoint = dsp.randint(0, dsp.flen(g) - max(layer[0]))
        
        grains = ''
        for l, p in zip(layer[0], layer[1]):
            grain = dsp.cut(g, startpoint, l)
            grain = dsp.env(grain, 'phasor')
            grain = dsp.taper(grain, dsp.mstf(10))
            grain = dsp.pan(grain, p)
            
            grains += grain

        layers += [ dsp.env(grains, 'phasor') ]

    out += dsp.mix(layers)

dsp.write(out, 'spiderfall')
