# swap two numbers
def swap(a, b):
    b, a = a, b
    return a, b

if __name__ == "__main__":
    a, b = input("Enter two numbers:").split()
    print(swap(a, b))
