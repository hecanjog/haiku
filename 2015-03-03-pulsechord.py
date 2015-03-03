from pippi import dsp

g = dsp.read('sounds/seneca3bars.wav').data
beat = dsp.bpm2frames(112)

g = dsp.split(g, dsp.flen(g) / 48)

out = ''

osts = [ dsp.randchoose(g) for a in range(3) ]

for p in range(32):
    alts = [ dsp.randchoose(g) for a in range(4) ]

    for b in range(dsp.randint(4, 12)):
        out += osts[p % len(osts)]
        out += alts[b % len(alts)]

dsp.write(out, 'pulsechord')
