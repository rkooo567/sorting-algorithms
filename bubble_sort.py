from util import swap

def bubble_sort(lst):
	last_index = len(lst) - 1
	for _ in range(0, len(lst)):
		for i in range(0, last_index):
			if lst[i] > last_index:
				swap(lst, i, last_index)
		last_index -= 1
	