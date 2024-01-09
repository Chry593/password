# -*- coding: utf-8 -*-
"""
Password generator
"""
import random
def generate_password():
    """ generate a password with 12 elements """
    lower_case = "qwertyuioplkjhgfdsazxcvbnm"
    upper_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
    special = '!£$%&/=?^._-'
    numbers = "0123456789"
    pwd = ""
    for _ in range(3) :
        
        l_case =random.choice(lower_case)
        u_case = random.choice(upper_case)
        s = random.choice(special)
        n = random.choice(numbers)
        
        pwd +=  l_case + u_case + s + n
        
    return pwd

def generate_n_pwd(n):
    """ generate n password """
    passwords = set()
    for _ in range(n):
        pwd = generate_password()
        passwords.add(pwd)
    return passwords

        

def save_on_file_random_pwd(fname,n):
    """ fname file , n password to generate """
    pwd = generate_n_pwd(n)
    with open (fname , mode ="a" , encoding="utf-8") as f:
        for passsword in pwd:
            f.write(f'{passsword}\n')


def pwd():
    print("==================")
    print("Password Generator")
    print("==================")    
    choice = input("1 : generate random passwords and save them in a file\nexit : close the generator\n")
    
    while True:
        
        if choice == "1":
            fname = input("file name: ")
            fname = f'{fname}.txt'
            n = int(input("number of password to generate: "))
            save_on_file_random_pwd(fname,n)
            return print('Passwords saved')
            
        elif choice == "exit":
            break
pwd()
    
    
