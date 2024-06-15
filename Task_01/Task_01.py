def calculate_area(length, width):
    return length * width

def main():
    rectangles = []
    
    for i in range(3):
        print(f"Enter dimensions for rectangle {i+1}:")
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        rectangles.append((length, width))
    
    for i, (length, width) in enumerate(rectangles):
        area = calculate_area(length, width)
        print(f"The area of rectangle {i+1} is: {area}")

if __name__ == "__main__":
    main()

