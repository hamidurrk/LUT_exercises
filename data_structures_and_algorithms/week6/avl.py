class AVLNode:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.height = 1

	def balance(self):
		left_height = self.left.height if self.left else 0
		right_height = self.right.height if self.right else 0
		return right_height - left_height

class AVL:
	def __init__(self):
		self.root = None

	def insert(self, key):
		self.root = self.insert_help(self.root, key)

	def insert_help(self, node, key):
		if not node:
			return AVLNode(key)
		if key < node.key:
			node.left = self.insert_help(node.left, key)
		elif key > node.key:
			node.right = self.insert_help(node.right, key)
		else:
			return node
		node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
		balance = node.balance()
		if balance < -1:
			if key < node.left.key:
				return self.right_rotation(node)
			else:
				return self.left_right_rotation(node)
		if balance > 1:
			if key > node.right.key:
				return self.left_rotation(node)
			else:
				return self.right_left_rotation(node)
		return node

	def get_height(self, node):
		return node.height if node else 0

	def right_rotation(self, y):
		x = y.left
		T2 = x.right
		x.right = y
		y.left = T2
		y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
		x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
		return x

	def left_rotation(self, x):
		y = x.right
		T2 = y.left
		y.left = x
		x.right = T2
		x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
		y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
		return y

	def left_right_rotation(self, node):
		node.left = self.left_rotation(node.left)
		return self.right_rotation(node)

	def right_left_rotation(self, node):
		node.right = self.right_rotation(node.right)
		return self.left_rotation(node)

	def preorder(self):
		result = []
		def helper(node):
			if not node:
				return
			bal = node.balance()
			sign = ''
			if bal > 0:
				sign = '+'
			elif bal < 0:
				sign = '-'
			result.append(f"{node.key}{sign}")
			helper(node.left)
			helper(node.right)
		helper(self.root)
		print(' '.join(result))

if __name__ == "__main__":
	Tree = AVL()
	for key in [9, 10, 11, 3, 2, 6, 4, 7, 5, 1]:
		Tree.insert(key)
	Tree.preorder()
