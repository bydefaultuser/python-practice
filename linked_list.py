class Node():
	def __init__(self,data):
		self.data = data
		self.next = None 
class LinkedList():
	def __init__(self):
		self.head = None
	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node 
		else:
			current = self.head
			while current.next != None:
				current =current.next  	
			current.next = new_node
	def display(self):
		current = self.head
		while current != None:
		
			print(current.data)
			current = current.next
	def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def search(self, value):
			
		current = self.head
		while current != None:
			if current.data == value:
				return True
			current = current.next
		return False
	def delete(self, value):
		if self.head is None:
			return False 
		if self.head.data == value:
			self.head = self.head.next
			return True
		
		current = self.head
		while current.next != None:
			if current.next.data == value:
				current.next = current.next.next 
				return True
			current = current.next
		return False
if __name__ == "__main__":
	d = LinkedList()
	d.append(4)
	d.append(5)
	d.append(6)
	d.display()
	d.prepend(2)
	d.display()
	d.delete(5)
	print(d.search(5))
	print(d.search(30))	
	d.display()
