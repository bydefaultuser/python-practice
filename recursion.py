def factorial(n):
	if n ==1:
		return 1
	else:
		return n* factorial(n-1)
def print_n_1(n):
	if n == 1:
		print(1) 
	else:
		print(n)
		print_n_1(n-1)
def sum_to_n(n):
	if n == 1:
		return 1 
	else:
		return n+ sum_to_n(n-1)
def fibonacci(n):
	if n == 1 or n == 2:
		return 1 
	else:
		return fibonacci(n-2)+fibonacci(n-1)

def array_sum(n):
	if len(n) == 0:
		return 0 
	else:
		return n[0] + array_sum(n[1:])
def reverse_string(s):
	if s == "":
		return ""
	else:
		return s[-1] + reverse_string(s[:-1])
		
		




			
if __name__ == "__main__":
	print(factorial(5))
	print_n_1(6)
	print(sum_to_n(10))
	print(fibonacci(5))
	print(array_sum([1,2,3,4]))
	print(reverse_string("hello"))
