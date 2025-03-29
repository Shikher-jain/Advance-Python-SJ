def evenOdd(x):
	"""Function to check if the number is even or odd"""
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")

# Driver code to call the function
print(evenOdd.__doc__)
print(evenOdd.__name__)
print(evenOdd.__code__)
print(evenOdd.__code__.co_varnames)