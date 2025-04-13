class ArithmeticOperations:
    """A class that provides basic arithmetic operations on two numbers."""
    
    def __init__(self, x: int, y: int):
        """
        Initialize the ArithmeticOperations class with two numbers.
        
        Args:
            x (int): First number
            y (int): Second number
        """
        self.x = x
        self.y = y

    def addition(self) -> float:
        """
        Add the two numbers.
        
        Returns:
            int: The sum of x and y
        """
        return self.x + self.y
    
    def subtraction(self) -> float:
        """
        Subtract y from x.
        
        Returns:
            int: The difference between x and y
        """
        return self.x - self.y
    
    def division(self) -> float:
        """
        Divide x by y.
        
        Returns:
            float: The quotient of x divided by y
            
        Raises:
            ZeroDivisionError: If y is zero
        """
        if self.y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.x / self.y
    
    def multiplication(self) -> float:
        """
        Multiply the two numbers.
        
        Returns:
            int: The product of x and y
        """
        return self.x * self.y
    