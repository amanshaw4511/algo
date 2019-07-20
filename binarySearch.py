#binary search

def bsearch(arr,i,j,data):
	if i==j:
		if arr[i]==data: return i
		else : return -1
	else:
		mid=(i+j)//2
		#print(arr[mid])
		if arr[mid]==data: return mid
		else:
			if data>arr[mid]:
				return bsearch(arr,mid+1,j,data)
			else:
				return bsearch(arr,i,mid-1,data)
				
def search(arr,data):
	return bsearch(arr,0,len(arr)-1,data)

a=[2,3,4,5,7,8,9,12]
print(search(a,96))