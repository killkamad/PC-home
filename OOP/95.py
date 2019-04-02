N=int(input("время жизни человека в секундах  "))
#DADA=N//10 #div
#KAKA=N%10    #mod
#print(DADA)
#print(KAKA)
count=0
while N//10>0:
	M=N
	N=0
	while M>0:
		M=M//10
		N=(N+M)%10
		count+=1
print("Полученная цифра",N)
print("Число преобразований",count)

		