
def merge(arr,lt,mid,rt):
	#devide arr in two sorted array
	left=list()
	right=list()
	n1=mid-lt+1	#len(left)
	n2=rt-mid		#len(right)
	#copy element to left & right arry
	for x in range(n1):
		left.append(arr[lt+x])
	for x in range(n2):
		right.append(arr[mid+x+1])
	
	#copy element to main arr in sorted order
	k=lt
	i=j=0
	while(i<n1 and j<n2):
		if left[i]<=right[j]:
			arr[k]=left[i]
			i+=1
			k+=1
		else:
			arr[k]=right[j]
			j+=1
			k+=1
	#checking if any element left
	while(i<n1):
		arr[k]=left[i]
		i+=1
		k+=1
	while(j<n2):
		arr[k]=right[j]
		j+=1
		k+=1
		

def mSort(arr,lt,rt):
	if lt<rt:
		mid=(lt+rt)/2
		mSort(arr,lt,mid)
		mSort(arr,mid+1,rt)
		merge(arr,lt,mid,rt)
	return arr


a=[33,6,74,6,74,3,6448,754,8]
print(mSort(a,0,len(a)-1))