x = [1,4,5,7,9,6,2,5,6,-3,-5,-10,15,34,4,6,4,8]
#x = [4,1,-2]
target = int(input("Vvedite chislo:"))
for i in x:
    if i < target:
        pair = int(target) - int(i)
        if pair in x:
            print ("Pervij= {} Vtoroij {}".format(i,pair))
            break