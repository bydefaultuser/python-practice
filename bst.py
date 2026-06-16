class Node():
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BST():
	def __init__(self):
		self.root = None
	def insert(self, data ):
		if self.root is None:
			self.root = Node(data)
		else:
			self._insert_helper(self.root, data)
	def _insert_helper(self, node, data):
		if data< node.data:
			if node.left is None:
				node.left = Node(data)
			else:
				self._insert_helper(node.left, data)
		else:
			if node.right is None:
				node.right = Node(data)
			else:
				self._insert_helper(node.right, data)
	def search(self, data):
		return self._search_helper(self.root, data)
	def _search_helper(self, node, data):
		if node is None:
			return False
		if node.data == data:
			return True
		if data< node.data:
			return self._search_helper(node.left, data)
		else:
			return self._search_helper(node.right, data)

	def inorder(self):
		return self._inorder_helper(self.root)
	def _inorder_helper(self, node):
		if node is None:
			return
		self._inorder_helper(node.left)
		print(node.data)
		self._inorder_helper(node.right)


if __name__ == "__main__":
	bst = BST()
	bst.insert(5)
	bst.insert(3)
	bst.insert(7)
	bst.insert(2)
	bst.insert(4)
	print(bst.search(4))
	print(bst.search(8))
	bst.inorder()
