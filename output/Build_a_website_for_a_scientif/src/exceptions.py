python
# src/exceptions.py

class InvalidInputError(Exception):
    """Raised when invalid input is provided."""
    pass

class DivisionByZeroError(Exception):
    """Raised when division by zero is attempted."""
    pass

class ZeroValueError(Exception):
    """Raised when a calculation result is zero."""
    pass

class NotANumberError(Exception):
    """Raised when a non-numeric value is used in a calculation."""
    pass

class OutOfRangeError(Exception):
    """Raised when a value is outside a valid range for a calculation."""
    pass

class UnknownOperationError(Exception):
    """Raised when an unknown mathematical operation is attempted."""
    pass

class IncompatibleTypeError(Exception):
    """Raised when incompatible types are used in a calculation."""
    pass
