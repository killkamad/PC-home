a= [
    [ -1,50,-1,600,-1,-1,-1],
    [ 50,-1,200,-1,-1,-1,-1],
    [ -1,200,-1,10,500,-1,-1],
    [ 600,-1,10,-1,400,-1,-1],
    [ -1,-1,500,400,-1,250,-1],
    [ -1,-1,-1,-1,200,-1,-1],
    [ -1,-1,-1,-1,-1,-1,-1],
]

labels = [float("inf")]*len(a)
plus =[False]*len(a)
start =0
end= 5
where= 0
labels[where]=0

while where!=end:
    plus[where]=True
    print('next city',where)
    for city in range(len(labels)):
        if a[where][city]!=-1 and not plus[city]:
            if a[where][city]+labels[where]<labels[city]:
                labels[city]=a[where][city]+labels[where]
    min=-1
    min_city=-1
    for i in range(len(labels)):
        if not plus[i]:
            if min==-1 or labels[i]<min:
                min=labels[i]
                min_city=i
    where=min_city

print(labels)

labels = [-1]*len(a)
