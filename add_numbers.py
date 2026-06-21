# Script to add two numbers and print the result

def get_number(prompt: str) -> float:
    """
    Prompts user for a number and validates input.
    
    Args:
        prompt: The prompt message to display to the user
        
    Returns:
        float: The validated number
        
    Raises:
        ValueError: If input cannot be converted to a number
    """
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            print(f"Error: '{user_input}' is not a valid number. Please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            raise SystemExit(1)


def add_numbers(num1: float, num2: float) -> float:
    """
    Adds two numbers and returns the result.
    
    Args:
        num1: First number
        num2: Second number
        
    Returns:
        float: The sum of num1 and num2
    """
    return num1 + num2


def main() -> None:
    """Main function to orchestrate the addition operation."""
    try:
        print("=== Simple Addition Calculator ===\n")
        
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        
        result = add_numbers(num1, num2)
        
        print(f"\nThe sum of {num1} and {num2} is {result}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
