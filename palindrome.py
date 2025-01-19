def is_palindrome(s):
    # Remove spaces and convert to lowercase for comparison
    cleaned_string = ''.join(e for e in s if e.isalnum()).lower()
    
    # Check if the string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Test the function
input_string = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
