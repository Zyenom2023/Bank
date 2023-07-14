import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            print("Error: Division by zero")

    def power(self, base, exponent):
        return base ** exponent

    def square_root(self, num):
        if num >= 0:
            return math.sqrt(num)
        else:
            print("Error: Invalid input for square root")

class PhysicsCalculator(Calculator):
    def calculate_velocity(self, initial_velocity, acceleration, time):
        return initial_velocity + (acceleration * time)

    def calculate_distance(self, initial_velocity, time, acceleration):
        return (initial_velocity * time) + (0.5 * acceleration * (time ** 2))

    def calculate_force(self, mass, acceleration):
        return mass * acceleration

# Example usage:
calculator = Calculator()

# Basic mathematical calculations
print(calculator.add(5, 3))  # Output: 8
print(calculator.subtract(10, 4))  # Output: 6
print(calculator.multiply(6, 2))  # Output: 12
print(calculator.divide(20, 5))  # Output: 4
print(calculator.power(2, 3))  # Output: 8
print(calculator.square_root(25))  # Output: 5

physics_calculator = PhysicsCalculator()

# Physics calculations
print(physics_calculator.calculate_velocity(10, 2, 5))  # Output: 20
print(physics_calculator.calculate_distance(10, 5, 2))  # Output: 85
print(physics_calculator.calculate_force(20, 5))  # Output: 100

