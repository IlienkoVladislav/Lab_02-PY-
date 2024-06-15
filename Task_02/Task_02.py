import math

def calculate_hypotenuse(a, b):
    """The hypothetical period behind two sides is discussed."""
    return math.sqrt(a**2 + b**2)

def main():
    print("Enter the sides for the first triangle:")
    a1 = float(input("Enter the first cathetus: "))
    b1 = float(input("Enter the second cathetus: "))
    
    print("Enter the sides for the second triangle:")
    a2 = float(input("Enter the first cathetus: "))
    b2 = float(input("Enter the second cathetus: "))
    
    hypotenuse1 = calculate_hypotenuse(a1, b1)
    hypotenuse2 = calculate_hypotenuse(a2, b2)
    
    if hypotenuse1 > hypotenuse2:
        print(f"The hypotenuse of the first triangle ({hypotenuse1}) is greater than the hypotenuse of the second triangle ({hypotenuse2}).")
    elif hypotenuse1 < hypotenuse2:
        print(f"The hypotenuse of the first triangle ({hypotenuse1}) is smaller than the hypotenuse of the second triangle ({hypotenuse2}).")
    else:
        print(f"The hypotenuses of both triangles are equal ({hypotenuse1}).")

if __name__ == "__main__":
    main()

