import string
import random
def get_random_string(length, line):
    # choose from all lowercase letter
    f = open("data.txt", "w")
    for i in range(line):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length)) 
        f.write(result_str + "\n")
        print("Random string of length", length, "is:", result_str)

get_random_string(10, 30)