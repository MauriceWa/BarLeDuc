# when user inputs a word, and it translates the meaning, also shows how many words match with the user input word
# dictionary_words = {1: "steve",
#                     2: "Josh",
#                     3: "Bob"
#                     }
#
# for key, value in dictionary_words.items():
#     print(key, value)


def dictionary():
    user_input = input("Input a word to translate")
    word_dict_db = {"accept": ["approval", "passed"],
                    "reject": "deny",
                    "correct": "right"
                    }

    # i = 0
    count_word = 0

    for key, value in word_dict_db.items():
        if user_input == key:
            count_word = count_word + 1
            print(count_word)
            print(f" The word you are looking for is {user_input}.\n This word means {value}, "
                  f"similar words count: {count_word}")


# while i < len(word_dict_db):
#     if user_input == word_dict_db:
#         print(word_dict_db[i])
#     else:
#         return

# first 3 digits of city last 5 of country
def thursday():
    city = {"Barcelona", "Zurich", "Krakow", "Moscow", "Barcelona"}
    city_list = ["Barcelona", "Zurich", "Krakow", "Moscow", "Barcelona"]
    city_name = "Amsterdam"
    country_name = 'Holland'
    message = city_name[:3] + ' ' + country_name[-5:]

    # print(city_list[-1], city_list[-2], city_list[-3])
    # print(city_list[-3:])
    # print(type(city_list[0]))
    # print(city_name[2:])
    print(message)


def thursday_two(input_by_user):
    mytuple = ()
    mytuple = mytuple + input_by_user
    print(type(mytuple))


def random():
    i = 0

    while i < 5:
        var = input("Input something")
        thursday_two(var)
        i = i + 1
        return var


def coordinates():
    xuser_input = input("What's your X coordinate?")
    yuser_input = input("What's your Y coordinate?")

    return xuser_input, yuser_input


# take 5 numbers from user and store it into a list,
# sort it and print it, print the minimum and maximum too, print total too
def calculator():
    user_list = []

    for i in range(0, 5):
        user_input = int(input(""))
        user_list.append(user_input)

        # print(min(user_list), max(user_list), sum(user_list))
    user_list = sorted(user_list)
    print(user_list)
    print(min(user_list), max(user_list), sum(user_list))





calculator()



