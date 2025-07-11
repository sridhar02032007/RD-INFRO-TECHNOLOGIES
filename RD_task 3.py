import random
import string

def generate_password(length):
    if length < 4:
        return "password length should be at least 4 characters for better "


    all_characters = string.ascii_letters + string.digits + string.punctuation


    password =[
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password += random.choice(all_characters )


    random.shuffle(password )

    return ''.join(password)
def main():
    print(" welcome to password generator")
    try:
        length=int(input("enter the lenght of the password "))
        password=generate_password(length)
        print(f"generate password:{password}")
    except ValueError:
        print("please enter valid number.")


if __name__=="__main__":
    main()
        
