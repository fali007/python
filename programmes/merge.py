def merge(array):
	if(len(array)>1):
		mid=len(array)//2
		left_half=array[:mid]
		right_half=array[mid:]

		merge(left_half)
		merge(right_half)

		i=0
		j=0
		k=0
		while i<len(left_half) and j<len(right_half):
			if(left_half[i]>right_half[j]):
				array[k]=right_half[j];
				j+=1
			else:
				array[k]=left_half[i];
				i+=1
			k+=1
		while i<len(left_half):
			array[k]=left_half[i]
			i+=1
			k+=1
		while j<len(right_half):
			array[k]=right_half[j]
			j+=1
			k+=1
arr=[9,5,6,7,1,4,2,3,0,8]
merge(arr)
print(arr)
