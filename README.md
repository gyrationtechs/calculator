# Calculator SDK

A simple SDK for performing basic arithmetic operations.

## Installation

You can install the SDK using pip:

```bash
pip install calculator-sdk
```

## Getting Started

### Basic Usage

1. Import the SDK:
```python
from calculator import ArithmeticOperations
```

2. Create an instance with two numbers:
```python
calculator = ArithmeticOperations(x=10, y=5)
```

3. Perform arithmetic operations:
```python
# Addition
result = calculator.addition()  # Returns 15

# Subtraction
result = calculator.subtraction()  # Returns 5

# Multiplication
result = calculator.multiplication()  # Returns 50

# Division
result = calculator.division()  # Returns 2.0
```

### Error Handling

The division operation includes error handling for division by zero:

```python
calculator = ArithmeticOperations(x=10, y=0)
try:
    result = calculator.division()
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Prints: Error: Cannot divide by zero
```

## Features

- Addition
- Subtraction
- Multiplication
- Division (with zero division protection)
- Type hints for better code completion
- Comprehensive documentation

## Requirements

- Python 3.7 or higher

## License

MIT License
