from pippi import dsp

g = dsp.read('sounds/seneca3bars.wav').data
beat = dsp.flen(g) / (12 * 13)
g = dsp.split(g, beat)

modulos = [3, 5, 7, 11]
numgrains = dsp.stf(20) / beat

streams = []
for mod in modulos:
    stream = []

    for i, s in enumerate(g):
        if i % mod == 0:
            stream += [ s ]

    stream = [ stream[i % len(stream)] for i in range(numgrains) ]

    streams += [ stream ]

out = []

for grain in range(numgrains):
    for stream in streams:
        out += stream[grain]

out = ''.join(out)

dsp.write(out, 'stringquilt')
