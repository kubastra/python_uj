def Zadanie_2_10():
    line = "ala ma\n10 kotow i psow\tborder collie"
    line = line.split()
    #print(line)
    count = 0
    for el in line:
        count += 1
    print(count) #8

def Zadanie_2_11():
    word = "Anaconda"
    letters = list(word)
    #print(letters)
    new_word = "_".join(letters)
    # for letter in letters:
    #     new_word = new_word + letter + '_'
    print(new_word)

def Zadanie_2_12():
    line = "ala ma\n10 kotow i psow\tborder collie"
    words = line.split()
    first_letters = ""
    last_letters = ""

    for word in words:
        first_letters += word[0]
        last_letters += word[-1]

    print("pierwsze: " + first_letters)
    print("ostatnie: " + last_letters)

def Zadanie_2_13():
    line = "ala ma\n10 kotow i psow\tborder collie"
    words = line.split()
    sum = 0
    for word in words:
        sum += len(word)

    print("suma: " + str(sum))

def Zadanie_2_14():
    line = "ala ma\n10 kotow i psow\tborder collie"
    words = line.split()

    len_words = len(words[0])
    max_word = words[0]

    for word in words:
        if len(word) > len_words:
            max_word = word
            len_words = len(word)

    print(max_word)
    print(len_words)

def Zadanie_2_15():
    L = [12, 305, 7, 89]
    word = ""
    for item in L:
        word += str(item)
    print(word)

def Zadanie_2_16():
    line = "Twórca Pythona to GvR."
    new_line = line.replace("GvR", "Guido van Rossum")
    print(new_line)

def Zadanie_2_17():
    line = "ala ma kota i psa border collie"
    words = line.split()
    sorteds = sorted(words)
    print(sorteds)
    sorteds = sorted(words, key=len)
    print(sorteds)

def Zadanie_2_18():
    number = 10020304500670
    string_number = str(number)
    count = string_number.count("0")
    print(count)

def Zadanie_2_19():
    L = [7, 24, 305, 1, 99]
    list = [str(x).zfill(3) for x in L]
    result = "".join(list)
    print(result)

if __name__ == "__main__":
    Zadanie_2_19()

