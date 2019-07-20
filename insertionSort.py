#insertion sort

def isort(arr):
	N=len(arr)
	i=j=0
	
	for _ in range(N-1):
		pnext= i+1 # pnext = pivot +1
		j=0
		for _ in range(pnext):
			if arr[j]>arr[pnext]:
				#swap
				arr[j],arr[pnext]=arr[pnext],arr[j]
			j+=1
		i+=1
	return arr


a=[39,46,2,78,32,7,3,7,3,67]
print(isort(a))
			