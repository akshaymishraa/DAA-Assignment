
def compAndSwap(a, i, j, dire): 
	if (dire==1 and a[i] > a[j]) or (dire==0 and a[i] < a[j]): 
		a[i],a[j] = a[j],a[i] 

def bitonicMerge(a, low, cnt, dire): 
	if cnt > 1:
		k = int(cnt/2)
		for i in range(int(low) , int(low+k)): 
			compAndSwap(a, i, i+k, dire) 
		bitonicMerge(a, low, k, dire) 
		bitonicMerge(a, low+k, k, dire)

def bitonicSort(a, low, cnt,dire):
	if cnt > 1:
		k = cnt/2
		bitonicSort(a, low, k, 1) 
		bitonicSort(a, low+k, k, 0)
		bitonicMerge(a, low, cnt, dire)
def sort(a,N, up): 
	bitonicSort(a,0, N, up) 

a = [0.7, 5.6, 2.3, 12, 45.23, 98.6, 1.98, 33.45]
n = len(a) 
arr=a[:]
arr.sort()
max_arr=arr[-1]
final=[]
for i in range(int(n/2)):
	final.append(arr[i])
final.append(max_arr)
arr.sort(reverse=True)
for i in range(1,int(n/2)):
	final.append(arr[i])
print('the Bitonic Sequence is:')
print(final)
up=1
sort(a, n, up) 
print ("Sorted array is")
print(a)
