#selection sort


def ssort(arr):
	N=len(arr)
	i=j=0
	for _ in range(N):
		minIndex=i
		j=i
		for _ in range(j,N):
			if arr[minIndex]>arr[j]: minIndex=j
			j+=1
		#swap
		arr[i],arr[minIndex]=arr[minIndex],arr[i]
		i+=1
	return arr
	
	
a=[2,46,22,83,22,73,24,5,45]
print(ssort(a))	
		