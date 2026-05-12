def check_password_strength(password):
    length = len(password)
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in "!@#$%^&*()_+-=[]{}|;:'\",.<>/?\\" for char in password)
    
    # Strength Logic
    if length < 8:
        return "Weak"
    elif length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        return "Strong"
    else:
        return "Medium"

# Main Program
print("🔐 Password Strength Checker")
password = input("Enter your password: ")

strength = check_password_strength(password)
print(f"Password Strength: **{strength}**")
