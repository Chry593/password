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
    a = 0
    while a < 3: 
        
        l_case =random.choice(lower_case)
        u_case = random.choice(upper_case)
        s = random.choice(special)
        n = random.choice(numbers)
        pwd +=  l_case + u_case + s + n
        a += 1
        
    return pwd

def choose_password():
    """ you can choose the password to save """
    pwd = generate_password()
    dict_for_pwd = {}
    print("password : {}".format(pwd))
    choice = 0
    i = 0
    while choice != 1:
        choice = input("Do you want to save? (y/n)\n")
        if choice == "y":
            dict_for_pwd[i] = pwd
            i += 1
            choice = int(input("1 : exit\n0 : regenerate password\n"))
            if choice == 1:
                break
            pwd = generate_password()
            print("password : {}".format(pwd))
        else:
            choice = int(input("1 : exit\n0 : regenerate password\n"))
            if choice == 1:
                break
            pwd = generate_password()
            print("password : {} ".format(pwd))
        
    return dict_for_pwd


def generate_n_pwd(n):
    """ generate n password """
    dict_pwd = {}
    a = 0
    while a < n:
        pwd = generate_password()
        dict_pwd[a] = pwd
        a += 1
    return dict_pwd


def save_on_file_choosen_pwd(fname):
    """ fname """
    pwd = choose_password()
    with open (fname , mode ="a" , encoding="utf-8") as f:
        for i,n in pwd.items():
            f.write(n)
            f.write("\n")
        

def save_on_file_random_pwd(fname,n):
    """ fname file , n password to generate """
    pwd = generate_n_pwd(n)
    with open (fname , mode ="a" , encoding="utf-8") as f:
        for i,n in pwd.items():
            f.write(n)
            f.write("\n") 


def pwd():
    print("==================")
    print("Password Generator")
    print("==================")    
    choice = input("1 : generate random passwords and save them in a file\n0 : choose the password to save\nexit : for close the generator\n")
    if choice == "1":
        fname = input("file name with the extension: ")
        n = int(input("number of password to generate: "))
        save_on_file_random_pwd(fname,n)
    elif choice == "0":
        fname = input("file name with the extension: ")
        save_on_file_choosen_pwd(fname)
    elif choice == "exit":
        return choice
        
    return "saved"
    
