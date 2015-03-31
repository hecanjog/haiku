from pippi import dsp

numboids = 100
numpoints = 1000

boids = [ [ dsp.rand(0, 1) for _ in range(numpoints + 1) ] for b in range(numboids) ]

for p in range(numpoints - 1):
    center = 0
    for b in boids:
        center += b[p]

    center = center / float(numboids)

    for i, b in enumerate(boids):
        boids[i][p+1] = boids[i][p] - ((center - boids[i][p]) / 1000.0)

out = []

freq = 300
wf = dsp.wavetable('sine2pi', 512)
win = dsp.wavetable('hann', 512)
length = dsp.stf(60)
pw = 1
modrange = 300
modfreq = 1.0 / 60

for b in boids:
    out +=  [ dsp.pulsar(freq, length, pw, wf, win, b, modrange, modfreq, 0.1) ]

out = dsp.mix(out)

dsp.write(out, 'boids')
