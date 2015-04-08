from pippi import dsp

snd = dsp.read('sounds/seneca3bars.wav').data

numgrains = 40 
lens = [ 1 for _ in range(numgrains/2) ]
lens = lens + dsp.wavetable('hann', numgrains)[len(lens):]
lens = [ dsp.mstf(l * 40 + 30) for l in lens ]

out = ''

lpos = 0
rpos = dsp.mstf(100)
for i in range(numgrains):
    l = dsp.cut(snd, lpos, lens[i])
    r = dsp.cut(snd, rpos, lens[i])

    lpos += dsp.mstf(dsp.rand(1, 10))
    rpos += dsp.mstf(dsp.rand(1, 10))

    out += dsp.pan(l, 0)
    out += dsp.pan(r, 1)

dsp.write(out, 'alter')
