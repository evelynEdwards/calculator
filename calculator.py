#4-operation calculator
def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b
        	
def circleArea(r):
	if r >= 0:
        	return 3.14 * r * r
	else:
        	return "Error"

def main():
	while True:
		a = float(input("First number: "))
		op = input("Operator (+ - * / a): ")
		b = float(input("Second number: "))
		if op == "+":
			print("Result:", add(a, b))
		elif op == "-":
			print("Result:", subtract(a, b))
		elif op == "*":
			print("Result:", multiply(a, b))
		elif op == "/":
			print("Result:", divide(a, b))
		elif op == "a":
			r = float(input("Radius: "))
			print("Result:", CircleArea(r))
		else:
			print("Unknown operator:", op)

if __name__ == "__main__":
	main()
