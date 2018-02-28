from util import swap, min_index

def selection_sort(lst):
	for i in range(0, len(lst)):
		minimum_index = min_index(lst, i, len(lst))
		swap(lst, i, minimum_index)
