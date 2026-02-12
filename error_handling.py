

import logging
logging.basicConfig(
    filename="error_log.log",     
    level=logging.ERROR,        
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class NegativeNumberError(Exception):
    """Raised when user enters a negative number."""
    pass


def divide_numbers(a, b):
    """Function to divide two numbers."""
    return a / b


def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num1 < 0 or num2 < 0:
            raise NegativeNumberError("Negative numbers are not allowed.")

        
        result = divide_numbers(num1, num2)
    

    except ValueError:
        print("Invalid input! Please enter numeric values.")
        logging.error("ValueError occurred due to invalid numeric input.")

    except ZeroDivisionError:
        print("Cannot divide by zero!")
        logging.error("ZeroDivisionError occurred.")

    except NegativeNumberError as e:
        print("Custom Error:", e)
        logging.error(f"NegativeNumberError: {e}")

    except Exception as e:
        print("Unexpected error occurred:", e)
        logging.error(f"Unexpected error: {e}")

    else:
        print("Division result:", result)

    finally:
        print("Execution completed.")


if __name__ == "__main__":
    main()
