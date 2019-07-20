#bubble sort

def bsort(arr):
	N=len(arr)
	i=j=0
	for _ in range(N):
		j=i
		for _ in range(j,N):
			if arr[i]>arr[j]: # swap
				arr[i],arr[j] = arr[j],arr[i]
			j+=1
		i+=1
	return arr

a=[2,56,9,3,85,3,68,744]
print(bsort(a))