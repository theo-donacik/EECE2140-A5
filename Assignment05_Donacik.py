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


