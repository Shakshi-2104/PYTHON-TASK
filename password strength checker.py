def check_password_strength(password):
    # Check password length
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters."
    
    # Check for at least one lowercase letter
    if not any(c.islower() for c in password):
        return "Password should have at least one lowercase letter."
    
    # Check for at least one uppercase letter
    if not any(c.isupper() for c in password):
        return "Password should have at least one uppercase letter."
    
    # Check for at least one digit
    if not any(c.isdigit() for c in password):
        return "Password should have at least one digit."
    
    # Check for at least one special character
    special_characters = "!@#$%^&*()_+[]{}|;:,.<>?/~`"
    if not any(c in special_characters for c in password):
        return "Password should have at least one special character."
    
    # If all checks pass
    return "Your password is strong!"

# Get user input
password = input("Enter your password: ")
result = check_password_strength(password)

# Display the result
print(result)
