from pippi import dsp
from pippi import tune

roots = tune.fromdegrees([2,6,9], octave=0, root='a')

def getPartials(roots, maxfreq=10000):
    minfreq = min(roots)

    partials = []

    for root in roots:
        currentfreq = 0
        mult = 1
        while currentfreq <= maxfreq:
            currentfreq = root * mult
            if currentfreq <= maxfreq:
                partials += [ currentfreq ]
                mult += 1

    return sorted(set(partials).union())

partials = getPartials(roots)

maxpartial = max(partials)
minpartial = min(partials)
numgrains = 1000

b1 = dsp.breakpoint([ dsp.rand(minpartial, maxpartial) for r in range(10) ], numgrains)
b2 = dsp.breakpoint([ dsp.rand(minpartial, maxpartial) for r in range(10) ], numgrains)

def makeGrain(freq, length):
    grain = dsp.tone(length, freq, amp=dsp.rand(0.05, 0.1))
    grain = dsp.pan(grain, dsp.rand())
    return grain

out = []

for i in range(numgrains):
    grainlen = dsp.mstf(dsp.rand(30, 100))

    lowf = min(b1[i], b2[i])
    highf = max(b1[i], b2[i])

    stack = [ makeGrain(root, grainlen) for root in roots ]

    for partial in partials:
        if partial >= lowf and partial <= highf:
            stack += [ makeGrain(partial, grainlen) ]

    stack = dsp.mix(stack)
    stack = dsp.env(stack, 'hann')

    out += [ stack ]

out = ''.join(out)

dsp.write(out, 'shapetones')
