
import re  
def validate_email(email):
    
    if not email:
        return False, 

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    if re.fullmatch(pattern, email):
        return True, 
    return False, 



def validate_mobile(mobile):

    if not mobile:
        return False, 

    pattern = r'^[6-9]\d{9}$'
    if re.fullmatch(pattern, mobile):
        return True, 
    return False, 

def validate_password(password):

    if not password:
        return False, 

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.fullmatch(pattern, password):
        return True, "Strong password."
    return False, (
        "Password must be 8+ characters with uppercase, lowercase, "
        "digit, and special character."
    )



def main():
    print("\n--- Regex Validation System ---")

    email = input("Enter email: ").strip()
    mobile = input("Enter Indian mobile number: ").strip()
    password = input("Enter password: ").strip()

    
    valid, message = validate_email(email)
    print("Email:", message)

    
    valid, message = validate_mobile(mobile)
    print("Mobile:", message)

  
    valid, message = validate_password(password)
    print("Password:", message)


if __name__ == "__main__":
    main()
