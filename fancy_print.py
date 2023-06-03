import time

alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "!"]
user_string = str(input("Enter the string:\n"))
completing_list = []

for letter in user_string:
    # time.sleep(0.1)
    for alphabet in alphabet_list:
        if letter == alphabet:
            print("".join(completing_list) + str(letter))
            completing_list.append(letter)
            time.sleep(0.1)
            break
        else:
            print("".join(completing_list) + alphabet)
            time.sleep(0.1)

time.sleep(0.69)
# nice
