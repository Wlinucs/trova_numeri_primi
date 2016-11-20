from math import sqrt  
import time
from threading import Thread

def ciao():
	print("inserisca il numero:")
	N=int(input(""))
	def trova_primi(n):    
		primi = [2]  
		for i in range(3, N, 2):  
			j = 0  
			while primi[j] <= sqrt(i):  
				if i%primi[j] == 0 : break  
				j = j+1  
			else:  
				primi.append(i)  
		return primi  
	print (trova_primi(N))
	print("vuoi dare un nome al file oppure lo salvo con il numero dei numeri?")
	b=input("scrivi 's' per rinominare, premi invio per usare il numero: ")
	if b=="s": 
		d=input("metti il nome:")
		m=d+".txt"
		q=open(m, "w")
		q.write(str(trova_primi(N)))
		q.close()
	else :
		a=str(N)+".txt"
		e=open(a, "w")
		e.write(str(trova_primi(N)))
		e.close()
t=Thread(target=ciao)
t.start()
t.join()