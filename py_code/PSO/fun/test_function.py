class Test_fun():
	def __init__(self):
		self = self
	def Sphere_function(self, x):
		sum = 0
		length = len(x)
		x = x**2
		for i in range(length):
			sum += x[i]
		return sum
