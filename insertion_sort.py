from util import swap

def insertion_sort(lst):
	for i in range(0, len(lst)):
		for j in range(0, i):
			if lst[j] > lst[i]:
				swap(lst, i, j)

lst = [2, 3, 4, 7, 8, 1, 5, 9, 6]
insertion_sort(lst)
print(lst)
