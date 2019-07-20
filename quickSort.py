#quick sort

def partition(arr,lt,rt):
    pivot = arr[rt]
    pIndex = lt
    for i in range(lt,rt):
        if arr[i]<=pivot:
            arr[i],arr[pIndex]=arr[pIndex],arr[i] #swap a[i],a[pIndex]
            pIndex+=1
    arr[pIndex],arr[rt]=arr[rt],arr[pIndex]     #swap a[pIndex],a[rt]
    return pIndex


def qSort(arr,lt,rt):
    if lt<rt:
        pIndex = partition(arr,lt,rt)
        qSort(arr,lt,pIndex-1)
        qSort(arr,pIndex+1,rt)
    return arr

a =[3,43,535,435,3,5,3,53,22,345]
print qSort(a,0,len(a)-1)
        
