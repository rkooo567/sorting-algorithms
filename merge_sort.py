from util import swap

def merge_sort(lst):
	"""
		choose a pivot index
		merge sort the left part
		merge sort the right part
		sort in ascending order
		*** merge sort is not destructive
	"""
	if len(lst) == 1:
		return [lst[0]]
	pivot = median(lst)
	left = merge_sort(lst[:pivot])
	right = merge_sort(lst[pivot:])
	sorted_lst = sort_helper(left, right)
	return sorted_lst

def sort_helper(left, right):
	"""
		Iterate through the left and right array and
		return the list that is sorted
	"""
	left_index = 0
	right_index = 0
	sorted_lst = []
	while left_index != len(left) and right_index != len(right):
		if left[left_index] >= right[right_index]:
			sorted_lst.append(right[right_index])
			right_index += 1
		else:
			sorted_lst.append(left[left_index])
			left_index += 1
	if left_index == len(left):
		sorted_lst += right[right_index:]
	else:
		sorted_lst += left[left_index:]
	return sorted_lst

def median(lst):
	"""
		Return the median index
	"""
	return len(lst) // 2
