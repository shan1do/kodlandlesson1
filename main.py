my_dict = {"ЛОЛ": "очень смешно",
          "КРИНЖ": "что-то странное, стыдное",
          "РОФЛ": "шутка",
          "ЩИЩ": "одобрение или восторг",
          "КРИПОВЫЙ": "страшный, пугающий"}

word = input("Непонятное слово").upper()


if word in my_dict.keys():
    print(my_dict[word])

else:
    print("Такого слова ещё нету")
    