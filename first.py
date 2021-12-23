
def callfunc(num1, num2):
    print(f"Calling this function now...")
    return num1 + num2


def main():
    result = callfunc(4, 5)
    print(f"Final output is {result}")

if __name__ == "__main__":
    main()