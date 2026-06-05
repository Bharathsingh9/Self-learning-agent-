python
# src/formats.py

class FormatError(Exception):
    pass

class FormatType:
    NUMBER = 'number'
    INTEGER = 'integer'
    STRING = 'string'
    BOOLEAN = 'boolean'

class Validator:
    @staticmethod
    def number(value):
        try:
            float(value)
            return True
        except ValueError:
            raise FormatError(f"Invalid number format: {value}")

    @staticmethod
    def integer(value):
        try:
            int(value)
            return True
        except ValueError:
            raise FormatError(f"Invalid integer format: {value}")

    @staticmethod
    def string(value):
        if not isinstance(value, str):
            raise FormatError(f"Expected string, got {type(value)}")
        return True

    @staticmethod
    def boolean(value):
        if not isinstance(value, bool):
            raise FormatError(f"Expected boolean, got {type(value)}")
        return True

    @staticmethod
    def check_type(value, expected_type):
        if not isinstance(value, expected_type):
            raise FormatError(f"Expected {expected_type}, got {type(value)}")

    @staticmethod
    def check_format(value, format_type):
        if format_type == FormatType.NUMBER:
            return Validator.number(value)
        elif format_type == FormatType.INTEGER:
            return Validator.integer(value)
        elif format_type == FormatType.STRING:
            return Validator.string(value)
        elif format_type == FormatType.BOOLEAN:
            return Validator.boolean(value)
        else:
            raise FormatError(f"Invalid format type: {format_type}")

# Example usage:
if __name__ == "__main__":
    # Valid usage
    try:
        print(Validator.check_format("10.5", FormatType.NUMBER))  # Returns True
        print(Validator.check_format("10", FormatType.INTEGER))  # Returns True
        print(Validator.check_format("Hello", FormatType.STRING))  # Returns True
        print(Validator.check_format(True, FormatType.BOOLEAN))  # Returns True
    except FormatError as e:
        print(f"Error: {e}")

    # Invalid usage
    try:
        print(Validator.check_format("abc", FormatType.NUMBER))  # Throws error
        print(Validator.check_format(123, FormatType.STRING))  # Throws error
    except FormatError as e:
        print(f"Error: {e}")
