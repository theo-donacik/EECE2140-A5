class BasicMathOperations:
  def greet(self, first, last):
    """Prints a greeting with first and last name.
    
    Args:
        first (string): The first name.
        number2 (string): The last name.
        
    Returns:
        void: No return but prints the output
    """
    print("Hello", first, last + "!")

  def add_numbers(self, number1, number2):
    """Sum two numbers and return the summation.
    
    Args:
        number1 (int/float): The first number.
        number2 (int/float): The second number.
        
    Returns:
        int/float: The sum of number1 and number2.
    """
    return number1 + number2

  def operation(self, number1, number2, operation):
    """Take two numbers and return the result of the operation.
    
    Args:
        number1 (int/float): The first number.
        number2 (int/float): The second number.
        operation (string): The operation
        
    Returns:
        int/float: The result of the operation on number1 and number2.
    """
    match operation:
      case "+":
        return number1 + number2
      case "-":
        return number1 - number2
      case "*":
        return number1 * number2
      case "/":
        return number1 / number2
      case _:
        raise Exception("Invalid Operation")

  def calculateSquare(self, num):
    """Gets the square of num
    
    Args:
        num (int/float): The number.
                
    Returns:
        int/float: The square of num
    """
    return num ** 2

  def factorial(self, num):
    """Gets the factorial of num
    
    Args:
        num (int/float): The number.
                
    Returns:
        int/float: The factorial of num
    """
    fact = 1
    for i in range(num):
      fact *= i+1
    return fact

  def counting(self, start, end):
    """Prints count from start to end
    
    Args:
        start (int/float): The starting number.
        end (int/float): The ending number.
                
    Returns:
        void: No return but prints the result
    """
    print(*[*range(start, end+1)])


  def calculateHypotenuse(self, base, perpindicular):
    """Gets the hypotenuse of a right angle triangle given the base and perpindicular
    Args:
        base (int/float): The base length of the triangle.
        perpindicular (int/float): The perpindicular length of the triangle.
                
    Returns:
        int/float: The hypotenuse 
    """
    return ((self.calculateSquare(base) + self.calculateSquare(perpindicular)) ** .5)

  def area(self, width, height):
    """Gets the area of a rectangle given a width and height
    Args:
        width (int/float): The width of the rectangle.
        height (int/float): The height of the triangle.
                
    Returns:
        int/float: The area
    """
    return width * height

  def power(self, base, exponent):
    """Gets the base to the power of exponent
    Args:
        base (int/float): The base number.
        exponent (int/float): The exponent number.
                
    Returns:
        int/float: Base ^ exponent
    """
    return base ** exponent

  def type(self, val):
    """Gets the type of val
    Args:
        val (int/float): The value to get the type of.
                
    Returns:
        string: The type of val  
    """
    return type(val).__name__

def main():
  math = BasicMathOperations()
  inpt = -1
  while inpt != 10:
    inpt = int(input("""[0] Greeting
[1] Add
[2] Operation
[3] Square
[4] Factorial
[5] Count
[6] Hypotenuse
[7] Area
[8] Power
[9] Type
[10 Quit]
What would you like to do: """))

    try:
      match inpt:
        case 0: math.greet(input("First name: "), 
                           input("Last name: "))
        case 1: print("The sum is", str(math.add_numbers(int(input("Num 1: ")),
                                                         int(input("Num 2: ")))))
        case 2: print("The result is", str(math.operation(int(input("Num 1: ")),
                                                          int(input("Num 2: ")),
                                                          input("Operator: "))))
        case 3: print("The square is", str(math.calculateSquare(int(input("Number: ")))))
        case 4: print("The factorial is", str(math.factorial(int(input("Number: ")))))
        case 5: math.counting(int(input("Start: ")), int(input("End: ")))
        case 6: print("The hypotenuse is", str(math.calculateHypotenuse(int(input("Base: ")),
                                                                        int(input("Perpandicular: ")))))
        case 7: print("The area is", str(math.area(int(input("width: ")),
                                                   int(input("height: ")))))
        case 8: print("The power is", str(math.power(int(input("base: ")),
                                                     int(input("exponent: ")))))
        case 9: print("The type is", str(math.type(input("Value: "))))
        case 10: print("Bye!") 
        case _: print("Invalid option")
    except:
      print("Invalid input. Try again")

main()
