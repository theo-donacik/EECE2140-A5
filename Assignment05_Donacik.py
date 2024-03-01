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


