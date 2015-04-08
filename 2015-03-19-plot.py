from matplotlib import pyplot as pp
from pippi import dsp
from hcj import data

length = dsp.stf(3)

curves = tuple([ data.Logistic(dsp.rand(3.8, 4), 0.1, length).data for _ in range(3) ])
y = [ (a * b * c) / 3.0 for a,b,c in zip(*curves) ]

freq = (1.0 / 3) / 200.0
amp = 0.5

out = dsp.ctone(freq, length, y, amp)
dsp.write(out, 'plot')

#x = range(len(y))
#pp.plot(x, y)
#pp.grid(True)
#pp.show()
