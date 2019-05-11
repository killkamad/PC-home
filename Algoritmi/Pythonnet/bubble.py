a = [1,3,5,2,4,1,6,5,7,8,5,4,3,2,1]
swap = True
while swap:
    swap = False
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
            swap = True
    print('next iteration',a,swap)

print(a)
