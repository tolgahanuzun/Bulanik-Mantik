import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd

def ayrikgrafik():
	t =  np.arange(0.0, 9.0, 1)
	s =  np.array([0.2,0.4,0.6,0.8,1,0.6,0.4,0.1,0])

	fig = plt.figure(figsize=(6, 6))
	vax = fig.add_subplot(111)

	vax.plot(t, s, 'o')
	vax.vlines(t, [0], s)


	plt.savefig('example/bulanik-ayrikyapi.png')
	plt.show() 