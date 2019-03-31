def swap(a,b):
	temp=a
	a=b
	b=temp

def quicksort(array):
	key=array[len(array)-1]
	k=0
	if len(array)!=0:
		for i in range(0,len(array)-1):
			if(array[i]<key):
				temp=array[i]
				array[i]=array[k]
				array[k]=temp
				k+=1
			if(i==len(array)):
				temp=array[len(array)-1]
				array[len(array)-1]=array[k]
				array[k]=temp
				quicksort(array[:k-1])
				quicksort(array[k+1:])





a=[2,3,4,5,6,7,8,1,23,4,512,32,4,43,54,65,7,66,54,3,43,54,345,35]
quicksort(a)
for i in range(0,len(a)):
	print(a[i])

	
def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)