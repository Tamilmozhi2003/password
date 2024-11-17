import random
import string
def generate_password(low,complexity ):
    if complexity == 'low':
        characters = string.ascii_lowercase  
    elif complexity == 'medium':
        characters = string.ascii_letters 
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits  
    elif complexity == 'very_high':
        characters = string.ascii_letters + string.digits + string.punctuation 
    else:
        return "Invalid complexity level."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Welcome to the Password Generator")
length = int(input("Enter the desired length of the password: "))
complexity = input("Enter the complexity level (low, medium, high, very_high): ").lower()
password = generate_password(length,complexity)
print(f"Generated Password: {password}")