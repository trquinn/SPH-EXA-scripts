import pynbody

infile = 'snapshot.001500'
outfile = 'nostar.std'

gstar = pynbody.load(infile)

print 'star mass: ', gstar.s['mass']
print 'star eps: ', gstar.s['eps']
print 'star pos: ', gstar.s['pos']
print 'star vel: ', gstar.s['vel']

# transform to astrocentric coordinates
pynbody.transformation.inverse_xv_translate(gstar, gstar.s['pos'][0],
					    gstar.s['vel'][0])
gstar.g.write(filename=outfile, fmt=pynbody.tipsy.TipsySnap)
