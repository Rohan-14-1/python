def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    
    if num1 < 0 or num2 < 0:
        print("Please enter positive integers.")
    else:
        greatest_common_divisor = gcd(num1, num2)
        print(f"The greatest common divisor of {num1} and {num2} is: {greatest_common_divisor}")

if __name__ == "__main__":
    main()

