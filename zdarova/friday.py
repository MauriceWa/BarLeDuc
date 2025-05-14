import pandas as pd


# take user input as int then show an error if not int
def questionnaire():
    user_i = input()

    try:
        int(user_i) / 0
    except ValueError:
        print("Input is not an integer")
    except ZeroDivisionError:
        print("Cant divide by zero")
        # print(type(user_i_int))
    finally:
        print("Have a good day!")
    # except:


# take input from user and output into the other function, a display function


def display(user_input):
    print(user_input)


def replay():
    user_input = input("Input your stuff: ")
    display(user_input)
    return int(user_input)


# input_by_user = preplay()
#
# print(type(input_by_user))


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT'],
    'Salary': [50000, 60000, 55000, 52000, 62000],
    'Bonus': [5000, 7000, 4000, 6000, 8000]
}

# df = pd.DataFrame(data)
# # display(df.head(2))
# # display(df.tail(2))
# # display(df.info())
# # display(df.describe())
# display(df[(df['Salary'] > 55000) & (df['Bonus'] > 7500)])

df = pd.read_csv('test.csv')
display(df[(df['Department'] == 'HR') & (df['Salary'] > 5000)])

