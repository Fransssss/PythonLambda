# Author: Fransiskus Agapa

# ========================
# simple program to operate basic math operation
# use lambda to make operation simpler
# ========================

from operation import addition
from operation import subtraction
from operation import  multiplication
from operation import division
from operation import module

# ========================

print("\n== Basic Math Operation ==")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Module")
print("e. exit")
choice = input("choice: ").lower()      # make user input to lower case to make while-loop condition simpler

while choice != 'e':
    if choice == '1':
        print("\n -- Addition --\n")
        try:                            # in case user input is not digit
            print("Input first number: ", end='')
            st_num = int(input())
            print("Input second number: ", end='')
            nd_num = int(input())
            add_val = addition(st_num, nd_num)
            print("\n[ " + str(st_num) + " + " + str(nd_num) + " = " + str(add_val) + " ]")
        except ValueError:
            print("\n[ Invalid input - digit only ]")

    elif choice == '2':
        print("\n -- Subtraction --\n")
        try:
            print("Input first number: ", end='')
            st_num = int(input())
            print("Input second number: ", end='')
            nd_num = int(input())
            sub_val = subtraction(st_num, nd_num)
            print("\n[ " + str(st_num) + " + " + str(nd_num) + " = " + str(sub_val)  + " ]")
        except ValueError:
            print("\n[ Invalid input - digit only ]")

    elif choice == '3':
        print("\n -- Multiplication --\n")
        try:
            print("\nInput first number: ", end='')
            st_num = int(input())
            print("Input second number: ", end='')
            nd_num = int(input())
            mul_val = multiplication(st_num, nd_num)
            print("\n[ " + str(st_num) + " + " + str(nd_num) + " = " + str(mul_val) + " ]")
        except ValueError:
            print("\n[ Invalid input - digit only ]")

    elif choice == '4':
        print("\n -- Division --\n")
        try:
            print("\nInput first number: ", end='')
            st_num = int(input())
            print("Input second number: ", end=' ')
            nd_num = int(input())
            div_val = division(st_num, nd_num)
            print("\n[ " + str(st_num) + " + " + str(nd_num) + " = " + str(int(div_val)) + " ]")  # result to be int
        except ValueError:
            print("\n[ Invalid input - digit only ]")

    elif choice == '5':
        print("\n -- Module --\n")
        try:
            print("\nInput first number: ", end='')
            st_num = int(input())
            print("Input second number: ", end='')
            nd_num = int(input())
            mod_val = module(st_num, nd_num)
            print("\n[ " + str(st_num) + " + " + str(nd_num) + " = " + str(mod_val) + " ]")
        except ValueError:
            print("\n[ Invalid input - digit only ]")

    else:
        print("\n[ Invalid choice ]")

    print("\n== Basic Math Operation ==")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Module")
    print("e. exit")
    choice = input("choice: ").lower()  # make user input to lower case to make while-loop condition simpler


print("\n== Exit Program ==")
