a = [
  [-1,-1,-1, 0,-1,-1,-1,-1,-1,-1,-1],
  [-1,-1, 0, 0, 0, 0,-1,-1,-1,-1,-1],
  [-1,-1, 0, 0, 0, 0,-1,-1,-1,-1,-1],
  [-1,-1, 0, 0, 0, 0,-1,-1,-1,-1,-1],
  [-1, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1],
  [-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0],
  [-1, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1],
  [-1,-1, 0, 0, 0, 0, 0, 0,-1,-1,-1],
  [-1, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1],
  [0 , 0,-1,-1,-1, 0, 0, 0,-1,-1,-1],
  [-1,-1, 0, 0, 0, 0, 0, 0,-1,-1,-1],
  [-1,-1, 0, 0, 0, 0,-1, 0, 0,-1,-1],
  [-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
  [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    
]

def out(a,way):
    print('-'*len(a[0])*3)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(j,i)in way:
                print(str(a[i][j]).rjust(3),end='')
            if a[i][j] ==-1:
                print('***',end='')
            else:
                print(str(a[i][j]).rjust(3),end='')
        print()
    print('-'*len(a[0])*3)


def step(a,k):
    changes=False
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]==k:
                if i< len(a)-1 and a[i+1][j] == 0:
                    a[i+1][j] = k+1
                    changes=True
                if i>0 and a[i-1][j] == 0:
                    a[i-1][j] = k+1
                    changes=True
                if j< len(a[i])-1 and a[i][j+1] == 0:
                    a[i][j+1] = k+1
                    changes=True
                if j>0 and a[i][j-1] == 0:
                    a[i][j-1] = k+1
                    changes=True
    return changes
#out(a,[])
x0=3
y0=7

x1=len(a[len(a)-1])-1
y1=len(a)-1

###########
k=1
a[y0][x0]=k
#out(a,way)
while step(a,k):
    k+=1

print('k= ',k)
x=x1
y=y1
k = a[y][x]
way= [(x,y)]
out(a,way)
while x != x0 or y != y0:
    if x>0 and a[y][x] == k-1:
        x=x-1
    elif y>0 and a[y-1][x] == k-1:
        y = y-1
    elif x< len(a[y])-1 and a[y][x+1] == k-1:
        x+=1
    elif y< len(a)-1 and a[y+1][x]== k-1:
        y=y+1
    way.append((x,y))
    k-=1


out(a,way)


