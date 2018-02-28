from util import swap

def quick_sort(lst):
	low = 0
	high = len(lst) - 1
	quick_sort_helper(lst, low, high)

def quick_sort_helper(lst, low, high):
	if low < high:
		partition_index = partition(lst, low, high)
		quick_sort_helper(lst, low, partition_index - 1)
		quick_sort_helper(lst, partition_index + 1, high)

def partition(lst, low, high):
	pivot = lst[high]
	wall_index = low - 1
	for i in range(low, high):
		if lst[i] < pivot:
			wall_index += 1
			swap(lst, i, wall_index)
	swap(lst, wall_index + 1, high)
	return wall_index + 1

