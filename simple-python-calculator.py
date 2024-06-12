import math


def main():
    print("***************************\n*****SIMPLE CALCULATOR*****\n***************************")
    print("\n")

    
    while True:
        try:
            print("#__Basic Operations__#\n1.Addition\n2.Subtraction\n3.Multipication\n4.Divition\n")
            print("#__Trigonometric Functions__# (Enter for x)\n5.Sin(x)\n6.Cos(x)\n7.Tan(x)\n")  
            print("#__Logarithmic Functions__# (Enter for x)\n8.log(x)\n9.log10(x)\n10.square root\n11.power -->(x(base),y(power))\n12.e^x\n")
            print("**Enter 13 to exit the programe**\n")

            user_option = int(input("Select the number for the option: "))

            if user_option > 13 or user_option < 1:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!Please Enter A Correct Number For Selected Operation!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                continue

            elif user_option == 13:
                print("Thank You for using the Simple Calculator")
                break

            elif user_option < 5 or user_option == 11:
                first_number, second_number = get_two_numbers()
                result = basic_operations(user_option, first_number, second_number)
                

            else:
                number = get_the_number()
                result = advance_operations(user_option, number)
                
            
            print(f"\n***************************\nAnswer: {result}\n***************************\n") 
            
        except ValueError:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!Please Enter the number!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            continue
        except ZeroDivisionError:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!You Can not Divide by Zero!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            continue
            


def get_two_numbers():
    while True:
        try:
            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))
            return first_number, second_number
        except ValueError:
            continue
                         
def get_the_number():
    while True:
        try:
            number = float(input("Enter the number: "))
            return number
        except ValueError:
            continue



def basic_operations(user_option, num1, num2):
    if user_option == 1:
        return num1 + num2
    elif user_option == 2:
        return num1 - num2
    elif user_option == 3:
        return num1 * num2
    elif user_option == 4:    
        return  num1 / num2 
    elif user_option == 11:
        return math.pow(num1,num2)
    



def advance_operations(user_option, num):
    if user_option == 5:
        return math.sin(num)
    elif user_option == 6:
        return math.cos(num)
    elif user_option == 7:
        return math.tan(num)
    elif user_option == 8:
        return math.log(num)
    elif user_option == 9:
        return math.log10(num)
    elif user_option == 10:
        return math.sqrt(num)
    elif user_option == 12:
        return math.exp(num)
            


if __name__ == "__main__":
    main()

