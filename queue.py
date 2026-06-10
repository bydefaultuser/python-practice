from collections import deque
class Queue():
	def __init__(self):
		self.items = deque()
	def enqueue(self,value):
		self.items.append(value)
	def dequeue(self):
		if self.is_empty():
			return None
		return self.items.popleft()
	def peek(self):
		if self.is_empty():
			return None
		return self.items[0]
	def is_empty(self):
		return len(self.items) ==0
	def size(self):
		return len(self.items)


if __name__ == "__main__":
	q = Queue()
	q.enqueue(2)
	q.enqueue(4)
	q.enqueue(7)
	print(f"peek:{q.peek()}")
	print(f"Dequeue:{q.dequeue()}")
	print(f"Dequeue:{q.dequeue()}")
	print(f"is empty:{q.is_empty()}")
	print(q)
