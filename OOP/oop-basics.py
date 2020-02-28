class Point():
	# pass

	# python constructor
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

# point1 = Point()
# point2 = Point()

# point1.x = 5
# point2.x = 10

# print(point1.x)
# print(point2.x)

# print(point1.getX())
# print(point2.getX())

point1 = Point(5, 10)
point2 = Point(1, 2)
point3 = Point(10, 100)

print(point1.getX())
print(point2.getX())
print(point3.getY())