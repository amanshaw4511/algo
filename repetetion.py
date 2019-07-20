#count repetetion

def rep(arr,MAX):
	n=len(arr)
	flags = [0 for x in range(MAX+1)]
	i=0
	
	for _ in range(n): 
		flags[arr[i]]+=1   
		i+=1
	
	#array to store count
	count=list()
	for x in arr:
		count.append(flags[x])
	return count
	
a=[1,1,1,6,6,8,8,9,9,9,9]
cnt=rep(a,9)
print(a)
print(cnt)
		
		
	