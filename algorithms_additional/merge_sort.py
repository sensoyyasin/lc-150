def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	mid = len(arr) // 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])

	return merge_two_sorted_arrays(left,right)

def merge_two_sorted_arrays(left,right):
	sorted_list = []
	i = j = 0
	
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			sorted_list.append(left[i])
			i += 1
		else:
			sorted_list.append(right[j])
			j += 1

	while i < len(left):
		sorted_list.append(left[i])
		i += 1

	while j < len(right):
		sorted_list.append(right[j])
		j += 1

	return sorted_list


arr = [70,50,30,10,20,40,60]
merged = merge_sort(arr)
print (merged)
