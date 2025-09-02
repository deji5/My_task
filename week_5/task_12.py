email = input("Enter your gmail: ").lower()
username, domain = email.split('@')
print(f"Username: {username}\nDomain: {domain}")