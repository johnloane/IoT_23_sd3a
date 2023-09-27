from sys import getsizeof

def main():
    #a = get_int()
    #b = get_int()
    #sum = add_two_numbers(a, b)
    #print(f"{sum}")
    jasons_hello()


def get_int():
    while True:
        try:
            a = input("Please enter an integer: ")
            return int(a)
        except:
            print("Please enter a valid integer")


def do_you_agree():
    while True:
        answer = input("Do you agree? ")
        if answer.lower() in ["y", "yes"]:
            return True
        elif answer.lower() in ["n", "no"]:
            return False
        

def jasons_hello(times=5):
    print("Hello\n" * times, end="")
    
    
    

def add_two_numbers(a, b):
    return a + b

words = set()

def check(word):
    if word.lower() in words:
        return True
    else:
        return False

def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        words.add(line.rstrip("\n"))
    file.close()
    return True

def size():
    return len(words)

#print("Hello, World!")

#name = input("What is your name? ")

#print(f"Hello, {name}")

#number = 2
#print(getsizeof(number))

main()



