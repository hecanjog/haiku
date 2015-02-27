from pippi import dsp
from pippi import tune

roots = tune.fromdegrees([1,3,5,9], octave=2, root='a')

maxfreq = 10000
minfreq = min(roots)

partials = []

for root in roots:
    lastfreq = 0
    mult = 1
    while lastfreq < maxfreq:
        lastfreq = root * mult
        partials += [ lastfreq ]
        mult += 1

partials = sorted(tuple(set(partials).union()))

numoscs = 20
numgrains = 1000
grainlen = dsp.mstf(100)

paths = []

for o in range(numoscs):
    paths += [ dsp.breakpoint([ dsp.rand() for r in range(dsp.randint(10, 100)) ], numgrains) ]

layers = []
for path in paths:
    grains = ''
    for pos in path:
        absfreq = pos * (maxfreq - minfreq) + minfreq

        cfreq = 0
        count = 0
        while absfreq > cfreq:
            cfreq = partials[count % (len(partials) - 1)]
            count += 1

        grains += dsp.env(dsp.pan(dsp.tone(grainlen, cfreq, amp=0.1), dsp.rand()), 'hann')

    layers += [ grains ]

out = dsp.mix(layers)

dsp.write(out, 'addsmear')
