import string
import random

#Exporting All the ascii words and digit which is used while creating a password.
small_letter = string.ascii_lowercase
big_letter = string.ascii_uppercase
digits = string.digits
pucntuation =  string.punctuation



def password_genrator(max_length=10,special_words=True,number=True,small=True,Capital=True):
    password = ""
    while(len(password)<max_length):
        if special_words:
            password += pucntuation[random.randint(0,len(pucntuation)-1)] 
        if number:
            password += digits[random.randint(0,len(digits)-1)]
        if small:
            password += small_letter[random.randint(0,len(small_letter)-1)]
        if Capital:
            password += big_letter[random.randint(0,len(big_letter)-1)]
        else:
            return "Please Provide The Needed Information!! "

    return password



def check_int(str):
    """
    This is Just to verify if the user giving correct vaule or not
    This Function is used to convert string digit value to int.
    if the user does not enter any number(1,2,3,4,5...etc) it will throw an Error and Take the input again from the User:

    Args:
        str : Takes an string value

    Returns:
        Int: After Checking everything working correctly it will return an integer value from the string
    """

    while(str.isdigit() == False):
        str = input("Please Enter The correct Number Value: ")
    return int(str)





if __name__ == "__main__":
    user_choice = check_int(input("Enter Maximum Length of your password: "))
    special_words = input("Do you Want Any Special Charachter? (y/n): ").lower() == "y"
    number = input("Do you Want Any number in Your Password? (y/n): ").lower() == "y"

    password_user = password_genrator(user_choice,special_words,number)
    print("\nGenrated Password is : ",password_user)
        


