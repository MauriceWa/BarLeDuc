NAME = "bob"
PASSWORD = 525


# ask for 2 numbers from the user, and display the sum of both

def hour_1():
    num1 = int(input("Please give me a number"))
    num2 = int(input("Please give me a second number"))
    print(num1 + num2)


# hour_1()


# get name user and password and check if it's correct, if its correct give confirmation and if not then catch error
# when user enters incorrect details, show what's wrong
# password has to be integer, and it has to be displayed when it is wrong
def hour_one():
    name = input("Whats your username?")
    password = int(input("Whats your password, it has to be a combination of numbers?"))

    # if password / 1 == password:
    #     print("Password is an integer")
    # else: print("Password is not an integer")

    if (name == NAME) and (password == PASSWORD):
        print("Login correct")
        return
    else:
        print(f"Login incorrect: {name} and {password} do not match the expected output. ")

    # elif name != NAME:
    #     # print(f"{name} is not correct")
    # elif password != PASSWORD:
    # print(f"{password} is not correct")

    # if name != NAME:
    #     print("Your username is incorrect.")
    #     return
    #
    # if password != PASSWORD:
    #     print("Your password is incorrect.")
    #     return
    # print("Successful login")


# program that generates numbers one to ten
# multiply each item in the list with 2
def hour_two():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    i = 0
    while i < len(nums):
        print(nums[i] ** 2)
        i = i + 1

# generate fruit names and their prices when user gives a fruit name
# check if both lists are the same length, if not give error
def hour_2():
    fruits = ["apple", "banana", "mandarin", "pear"]
    fruit_prices = [ 1.22, 4.99, 2]
    i = 0
    user_says = input("What fruit would you like")

    if len(fruits) != len(fruit_prices):
        print("The database has an error.")
        return

    while i < len(fruits):
        if user_says == fruits[i]:
            print(f" The {fruits[i]} costs ${fruit_prices[i]}")
        i = i + 1


# that has names of people, adres and phone numbers

def hour_twee():
    person_details = {"Name": "Josh",
                      "Street": "Applestreet 5",
                      "Phone number": 5}

    print(list(person_details.values()))
    # for key, value in person_details.items():
    #     print(f"{key}: {value}")

hour_twee()





# friday: 4 hours
# saturday: 6 hours I have an appointment at 13:00-15:00 my time
# sunday 4 hours I have the test at 20:00 my time






