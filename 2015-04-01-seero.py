from pippi import dsp

snd = dsp.read('sounds/seneca3bars.wav').data
snd = dsp.split(snd, 0, 1)
snd = dsp.packet_shuffle(snd, 3)
snd = [ s * dsp.randint(1, 10) for s in snd ]

out = ''.join(snd)

dsp.write(out, 'seero')
