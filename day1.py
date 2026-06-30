# writing a js code in py
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print(f"login successful")
else :
    print(f"invalid credentials")    

# ask for detals
valide_age = 18
username = str(input("enter your name: ")) 
age = int(input("enter your real age here: "))

if age >= valide_age:
    print(f"wolcome {username}, you are an adult")
else :  
    print(f"sorry {username}, you are underage")  

# create a list
languages = ["Python", "JavaScript", "TypeScript", "Rust"]

# Check both conditions
if "Python" in languages:
    print("✓ Python is in the list")
else:
    print("✗ Python is not in the list")

if "Java" not in languages:
    print("✓ Java is not in the list")
else:
    print("✗ Java is in the list")