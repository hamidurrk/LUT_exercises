def sums(items):
	possible = set([0])
	for item in items:
		new_sums = set()
		for s in possible:
			new_sums.add(s + item)
		possible.update(new_sums)
	possible.discard(0)
	return len(possible)

if __name__ == "__main__":
	print(sums([1, 2, 3]))
	print(sums([2, 2, 3]))
	print(sums([1, 3, 5, 1, 3, 5]))
	print(sums([1, 15, 5, 23, 100, 55, 2]))
