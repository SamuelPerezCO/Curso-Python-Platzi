numbers = [1,2,3,4,5]

squares = []

for number in numbers:
    square = number ** 2
    squares.append(square)

print(squares)

numbers = [1,2,3,4,5]

squares = [x**2 for x in numbers]
print(squares)

class Calculator:
    def add_numbers(self, first_number, second_number):
        result = first_number + second_number
        return result
    
calc = Calculator()
print(calc.add_numbers(5,3))