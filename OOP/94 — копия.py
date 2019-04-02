N=int(input("Число голов одним ударом  "))
M=int(input("Число голов дракона  "))
K=int(input("Число голов, которые дракон регенерирует  "))

count=0
if K>N and N<M:
	print("NO")
elif K==N and M>>K:
	print("NO")	
else:
	while M>0:
			count+=1	
			M=M-N
			if M>0:
				M+=K


	print(count)
