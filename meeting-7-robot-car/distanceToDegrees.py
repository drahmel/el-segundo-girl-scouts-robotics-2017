
def distanceToDegrees(distance):
	pi = 3.14159
	diameter = 2.125
	circumference = diameter * pi
	print("circumference", circumference)
	rotations = distance / circumference
	print("rotations", rotations)
	degrees = rotations * 360
	print("degrees", degrees)

distanceToDegrees(24)
