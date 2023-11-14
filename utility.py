def main():
    x = int(input("Enter a number: "))
    print('x squared is', square(x))


def square(x):
    return x * x


def hello(to="World"):
    return f"Hello, {to}"

if __name__ == '__main__':
    main()