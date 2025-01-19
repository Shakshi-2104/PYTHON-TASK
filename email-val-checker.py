import re
def is_valid_email(email):
    if "@" not in email:
        return False
    if "." not in email.split("@")[1]:
        return False
    if email.startswith("."):
        return False
    if email.endswith("."):
        return False
    if email.startswith("@"):
        return False
    if email.endswith("@"):
        return False
    if not re.match(r"[^@]+@[^@]+\.[^@]+",email):
        return False
    return True
    
email=input("enter an email address:")
if is_valid_email(email):
    print(f"The email address'{email}'is valid.")
else:
    print(f"The email address'{email}'is not valid.")
        
