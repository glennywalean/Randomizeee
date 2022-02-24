from os import system
from random import randint

def clear():
    system('clear')

def main_menu():
    while(True):
        clear()
        print("  ___              _           _                \n | _ \__ _ _ _  __| |___ _ __ (_)______ ___ ___ \n |   / _` | ' \/ _` / _ \ '  \| |_ / -_) -_) -_)\n |_|_\__,_|_||_\__,_\___/_|_|_|_/__\___\___\___|\n")
        print("Simple Random Number Generator Tool - [Glenny Walean]\n")
        
        print("[1]  Start")
        print("[2]  About The Author")
        print("[3]  Quit\n")

        menu = input("input : ")
        if(menu == '1'):
            start()
        elif(menu == '2'):
            about_the_author()
            pass
        elif(menu == '3'):
            exit()
        else:
            print("\nError : invalid input.")
            input("\n\n\t<<<press ENTER to continue>>>")

def start():
    clear()
    start = int(input("input start number        : "))
    end = int(input("input end number          : "))
    num_count = int(input("input random number count : "))
    print("\n")
    for i in range(num_count):
        random = randint(start, end)
        value = random
        print("Random number [{}]= {}".format(i+1, str(value)))
    input("\n\n\t<<<press ENTER to continue>>>")

def about_the_author():
    clear()
    print("A highly motivated computer science student who likes programming.")
    input("\n\n\n\n\n\t<<<press ENTER to continue>>>")

main_menu()