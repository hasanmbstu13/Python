def remove_last_item(L):
	""" (list) -> list

	Return list L with the last item removed.

	Precondition: len(L) >= 0

	>>> remove_last_item([1, 2, 3, 4])
	[1, 2, 3]
	"""

	del L[-1]
	return L