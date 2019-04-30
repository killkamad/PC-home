def sort(a,left,right):
    print('will sort from',left,'to',right)
    if left ==right:
        print(left,right,'go back')
        return
    middle = (left+right)//2
    sort(a,left,middle)
    sort(a,middle+1,right)
    merge(a,left,middle,right)
def merge(a,left,middle,right):
    b = []
    cl = left
    cr = middle + 1
    n = right - left + 1
    for i in range(n):
        if cl>middle:
            take = 'right'
        elif cr>right:
            take = 'left'
        elif a[cl] < a[cr]:
            take = 'left'
        else:
            take = 'right'
        if take =='left':
            b.append(a[cl])
            cl+=1
        else:
            b.append(a[cr])
            cr+=1
    for i in range(len(b)):
        a[i+left] = b[i]
    print(b)
w=[1,4,7,5,6,3,8,6,4,5,6,7,1]
sort(w,0,len(w)-1)

