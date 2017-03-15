import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd

def ayrikgrafik():
	t =  np.arange(0.0, 9.0, 1)
	s =  np.array([0.2,0.4,0.6,0.8,1,0.6,0.4,0.1,0])

	fig = plt.figure(figsize=(12, 7))
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
	
	fig = plt.figure(figsize=(12, 7))
	vax = fig.add_subplot(111)
	vax.plot(indisy,indisx)

	plt.savefig('example/bulanik-surekliyapi.png')
	plt.show() 

	

def ucgen():
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
	
	fig = plt.figure(figsize=(12, 7))
	vax = fig.add_subplot(111)
	vax.plot(indisy,indisx)

	l, = vax.plot(np.repeat(1, 6), '--')
	plt.axvline(3, color='b', linestyle='dashed', linewidth=2)

	plt.savefig('example/ucgenuyelik.png')
	plt.show()

def uyelikucgen(x1,xT,x2,indisy):
	indisx = []
	for x in indisy:
		a=(x-x1)/(xT-x1)
		b=(x2-x)/(x2-xT)
		c=0;
		indisx.append(max(min(a,b),c))
	return indisx

def ucgenodev():
	fig = plt.figure(figsize=(12, 7))
	vax = fig.add_subplot(111)
	plt.grid(True)
	vax.set_title('Yas Uyelik Ucgeni')

	indisy1 = np.arange(0.0, 20.1, 0.1)
	indisx1 = np.array(uyelikucgen(0,10,20,indisy1))	
	vax.plot(indisy1,indisx1,label='Cocuk', color='blue')
	vax.fill_between(indisy1, 0,indisx1, facecolor='blue', alpha=0.5)
	vax.legend(loc='upper left', shadow=True)

	indisy2 = np.arange(10.1, 40.1, 0.1)
	indisx2 = np.array(uyelikucgen(10,20,40,indisy2))
	vax.plot(indisy2,indisx2,label='Genc', color='orange')
	vax.fill_between(indisy2, 0,indisx2, facecolor='orange', alpha=0.5)
	vax.legend(loc='upper left', shadow=True)


	indisy3 = np.arange(20.1, 60.1, 0.1)
	indisx3 = np.array(uyelikucgen(20,40,60,indisy3))
	vax.plot(indisy3,indisx3,label='Orta Yasli', color='green')
	vax.fill_between(indisy3, 0,indisx3, facecolor='green', alpha=0.5)
	vax.legend(loc='upper left', shadow=True)


	indisy4 = np.arange(40.1, 60.1, 0.1)
	indisx4 = np.array(uyelikucgen(40,60,60,indisy4))
	vax.plot(indisy4,indisx4,label='Yasli', color='red')
	vax.fill_between(indisy4, 0,indisx4, facecolor='red', alpha=0.5)
	vax.legend(loc='upper left', shadow=True)


	plt.savefig('example/yasucgeni.png')
	plt.show()
#ucgenodev()	
def yamuk():
	indisy = np.arange(-2.0, 2.1, 0.1)
	indisx = []
	x1= -1.5
	xT1= -0.5
	xT2= 0.5
	x2= 1.5
	for x in indisy:
		a=(x-x1)/(xT1-x1)
		b=1.0
		c=(x2-x)/(x2-xT2)
		d=0.0
		indisx.append(max(min(min(a,c),b),d))

	indisx = np.array(indisx)
	
	fig = plt.figure(figsize=(12, 7))
	vax = fig.add_subplot(111)
	vax.plot(indisy,indisx)

	#l, = vax.plot(np.repeat(1, 6), '--')
	#plt.axvline(3, color='b', linestyle='dashed', linewidth=2)

	plt.savefig('example/yamukuyelik.png')
	plt.show()

def gaussian():
	indisy = np.arange(-5.0, 5.1, 0.1)
	indisx = []

	xT = 0
	w = 1.5
	for x in indisy:
		a= (x-xT)/w
		b= -(1/2)*(a**2)

		indisx.append(np.exp(b))

	indisx = np.array(indisx)
	
	fig = plt.figure(figsize=(12, 7))
	vax = fig.add_subplot(111)
	vax.plot(indisy,indisx)

	#l, = vax.plot(np.repeat(1, 6), '--')
	#plt.axvline(3, color='b', linestyle='dashed', linewidth=2)

	#plt.savefig('example/yamukuyelik.png')
	plt.show()
#gaussian()	