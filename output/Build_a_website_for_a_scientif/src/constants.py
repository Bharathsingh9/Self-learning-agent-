python
# src/constants.py

class Constants:
    OPERATIONS = {
        'add': '+',
        'subtract': '-',
        'multiply': '*',
        'divide': '/'
    }

    NUMBERS = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'negative zero', 'negative one', 'negative two', 'negative three', 'negative four',
        'negative five', 'negative six', 'negative seven', 'negative eight', 'negative nine'
    ]

    DECIMAL_PLACES = {
        'none': 0,
        'one': 1,
        'two': 2,
        'three': 3
    }

    ERROR_MESSAGES = {
        'invalid_number': 'Invalid number',
        'invalid_operation': 'Invalid operation',
        'division_by_zero': 'Cannot divide by zero',
        'not_enough_arguments': 'Not enough arguments for operation',
        'too_many_arguments': 'Too many arguments for operation',
        'undefined_operation': 'Undefined operation'
    }

    MAX_DECIMAL_PLACES = 3

    MIN_NUMBER = -1e308
    MAX_NUMBER = 1e308

    TOLERANCE = 1e-9

    # Supported number formats
    NUMBER_FORMATS = [
        '.', '-', '+', '(', ')'
    ]

    # Supported number separators
    NUMBER_SEPARATORS = [
        ',',
        '.'
    ]
