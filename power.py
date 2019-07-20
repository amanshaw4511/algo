#find pow(a,n)

def power(a,n):
	#print(a,n)
	#base case
	if n==1: return a
	if n==0: return 1
	# .......... 
	
	if n%2==0:
		p = power(a,n//2)
		return p*p
	else:
		p=power(a,(n-1)//2)
		return a*p*p

		
print(power(2,0))