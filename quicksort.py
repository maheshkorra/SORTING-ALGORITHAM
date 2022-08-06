def quicksort(arr):
    m=max(arr)
    p=0
    l=len(arr)
    
    while m>0:
        narr=[0]*l
        darr=[0]*l
        m=m//10
        p+=1
        for i in range(l):
            k=arr[i]%(10**p)
            k=k//(10**(p-1))
            darr[i]=k
        k=0
        for j in range(10):
            for i in range(l):
                if darr[i]==j:
                    narr[k]=arr[i]
                    k+=1
        arr=narr
    return arr

if __name__=='__main__':
    arr=[152,8562,7851,12,0,111]
    arr=quicksort(arr)
    print(arr)
