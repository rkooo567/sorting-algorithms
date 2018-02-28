import sys

def swap(lst, index_one, index_two):
	temp = lst[index_one]
	lst[index_one] = lst[index_two]
	lst[index_two] = temp

def min_index(lst, first_index, last_index):
	"""
		Return the minimum index in a list of range(first_index ~ last_index)
	"""
	minimum = lst[first_index]
	min_index = first_index
	for i in range(first_index, last_index):
		if lst[i] < minimum:
			minimum = lst[i]
			min_index = i
	return min_index

	