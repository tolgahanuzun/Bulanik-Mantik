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


def surekligrafik():
	indisy =  np.arange(0.0, 10.1, 0.1)
	indisx = []
	for indis in indisy:
		indisx.append(1./(1+10*((indis-5)**2)))
	indisx =np.array(indisx)	
	
	fig = plt.figure(figsize=(6, 6))
	vax = fig.add_subplot(111)
	vax.plot(indisy,indisx)

	plt.savefig('example/bulanik-surekliyapi.png')
	plt.show() 

	

def ucgenuyelik():
	indisy = np.arange(0.0, 5.1, 0.01)
	indisx = []
	x1=1
	xT=3
	x2=4
	for x in indisy:
		a=(x-x1)/(xT-x1)
		b=(x2-x)/(x2-xT)
		c=0;
		indisx.append(max(min(a,b),c))

	indisx = np.array(indisx)
	
	fig = plt.figure(figsize=(6, 6))
	vax = fig.add_subplot(111)
	vax.plot(indisy,indisx)

	l, = vax.plot(np.repeat(1, 6), '--')
	plt.axvline(3, color='b', linestyle='dashed', linewidth=2)

	plt.savefig('example/ucgenuyelik.png')
	plt.show()

ucgenuyelik()	
surekligrafik()
ayrikgrafik()