a = [
  [ 4, 3, 0, 0, 0, 0, 0],
  [ 0, 0, 0, 0, 0, 0, 0],
  [ 0, 2, 0, 0,-1, 0, 0],
  [ 0, 0, 0, 0, 0, 1, 0],
  [ 0, 0,-1, 0, 0, 0, 0],
  [ 4, 1, 0, 0, 0, 0, 4],
    
]


for i in range(len(a)-1):
    for j in range(len(a[i])):
        if a[i][j]>=a[0][0] and a[i][j]==1 and a[i-1][j]==0:
            a[i-1][j]=1
        elif i<=len(a)-1 and a[i-1][j]!=0:
            a[i-1][j] = a[i-1][j]
            
        if a[i][j]==2 and a[i][j+1]==0:
            a[i][j+1]=2
        elif j<=len(a)-1 and a[i][j+1]!=0:
            a[i][j+1]=a[i][j+1]
            
        if a[i][j]==3 and a[i+1][j]==0:
            a[i+1][j]=3
        elif i<=len(a)-1 and a[i+1][j]!=0:
            a[i+1][j]=a[i+1][j]
            
        if a[i][j]==4 and a[i][j-1]==0:
            a[i][j-1]=4
        elif j<=len(a)-1 and a[i][j-1]!=0:
            a[i][j-1]= a[i][j-1]
            
print(a)

