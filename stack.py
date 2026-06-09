class Stack:
	def __init__(self):
		self.item =[]

	def push(self, value):
		self.item.append(value)
	def pop(self):
		if self.is_empty():
			return None			
		return self.item.pop()
	def peek(self):
		if self.is_empty():
			return None
		return self.item[-1]
	def is_empty(self):
		return len(self.item) ==0
if __name__ == "__main__":
	
	s = Stack()
	s.push(5)
	s.push(6)
	s.push(8)
	s.push(10)
	print(f"Peek: {s.peek()}")
	print(f"pop: {s.pop()}")
	print(f"pop again {s.pop()}")
	print(f"is empty {s.is_empty()}")
