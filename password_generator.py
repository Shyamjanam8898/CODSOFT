import random
import string

def password_generator(length,lower,upper,digits,special):
    letter=lower
    
    if  upper:
        letter+=upper      
    if digits:
        letter+=digits                  
    if special:
        letter+=special   
    
    password=" ".join(random.choice(letter) for i in range(length))       #selecting any random letters form the given data
    return password

def main():
    print("Welcome to password generator!")
    
    lower=string.ascii_lowercase          #generate lower case letter from a-z
    upper=string.ascii_uppercase          #generate upper case letter from A-Z
    digits=string.digits                  #generates digits from 0-9
    special=string.punctuation            #generates special characters
    try:
        length=int(input("Enter a length of password (minimum 6): "))
    except ValueError:
        print("please enter a numeric value")
        exit(0)
    if length<6:
        print("Warning : for strong security, it is recommended to have a minimum 6 letter password ")
        exit(0)
    print("select complexity level:")
    print("1.Simple")
    print("2.Medium")
    print("3.Defficult")
    level=input("Enter the complexity number for the password: ")
    if level=='1':
        generate_password=password_generator(length,lower,upper,digits=False,special=False)
    elif level=='2':
        generate_password=password_generator(length,lower,upper,digits,special=False)
    elif level=='3':
        generate_password=password_generator(length,lower,upper,digits,special)
    else:
        print("Wrong input, please enter the valid complexity level number.")
        exit(0)
        
    print(f"Generated password: {generate_password}")

if __name__== "__main__":
    main()