def sum_of_digits(input_str):
    """
    Calculates the sum of all digits in the given string.

    Args:
        input_str: the string containing digits and other characters

    Returns:
        the sum of all digits in the string
    """
    sum = 0
    for i in input_str:
        if ord('0') <= ord(i) <= ord('9'):
            sum += ord(i) - ord('0')

    return sum


if __name__ == '__main__':
    input1 = "abc123"
    input2 = "5 cats and 2 dogs"
    input3 = "No digits here!"

    print(f"Sum of digits in '{input1}': {sum_of_digits(input1)}")  # Should be 6
    print(f"Sum of digits in '{input2}': {sum_of_digits(input2)}")  # Should be 7
    print(f"Sum of digits in '{input3}': {sum_of_digits(input3)}")  # Should be 0