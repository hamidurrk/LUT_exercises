class MinHeap:
	def __init__(self, A):
		self.heap = A[:]
		n = len(self.heap)
		for i in range((n // 2) - 1, -1, -1):
			self._sift_down(i)

	def print(self):
		print(' '.join(str(x) for x in self.heap))

	def push(self, key):
		self.heap.append(key)
		self._sift_up(len(self.heap) - 1)

	def pop(self):
		if not self.heap:
			return None
		min_val = self.heap[0]
		last = self.heap.pop()
		if self.heap:
			self.heap[0] = last
			self._sift_down(0)
		return min_val

	def _sift_up(self, idx):
		while idx > 0:
			parent = (idx - 1) // 2
			if self.heap[idx] < self.heap[parent]:
				self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
				idx = parent
			else:
				break

	def _sift_down(self, idx):
		n = len(self.heap)
		while True:
			left = 2 * idx + 1
			right = 2 * idx + 2
			smallest = idx
			if left < n and self.heap[left] < self.heap[smallest]:
				smallest = left
			if right < n and self.heap[right] < self.heap[smallest]:
				smallest = right
			if smallest != idx:
				self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
				idx = smallest
			else:
				break

if __name__ == "__main__":
	heap = MinHeap([4, 8, 6, 5, 1, 2, 3])
	heap.print()         
	print(heap.pop())   
	heap.push(9)
	heap.print()        
