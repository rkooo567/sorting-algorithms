import unittest

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
# from heap_sort import heap_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

class TestSort(unittest.TestCase):

	def test_bubble_sort(self):
		lst = [2, 3, 4, 7, 8, 1, 5, 9, 6]
		expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		bubble_sort(lst)
		self.assertEqual(lst, expected) 

	def test_insertion_sort(self):
		lst = [2, 3, 4, 7, 8, 1, 5, 9, 6]
		expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		insertion_sort(lst)
		self.assertEqual(lst, expected) 

	def test_selection_sort(self):
		lst = [2, 3, 4, 7, 8, 1, 5, 9, 6]
		expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		selection_sort(lst)
		self.assertEqual(lst, expected) 

	def test_quick_sort(self):
		lst = [2, 3, 4, 7, 8, 1, 5, 9, 6]
		expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		quick_sort(lst)
		self.assertEqual(lst, expected) 

	def test_merge_sort(self):
		lst = [2, 3, 4, 7, 8, 1, 5, 9, 6]
		expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		lst = merge_sort(lst)
		self.assertEqual(lst, expected) 

if __name__ == "__main__":
	unittest.main()