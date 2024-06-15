import math

def area_of_quadrilateral(X, Y, Z, T):
    d = math.sqrt(X**2 + Y**2)
    
    area_triangle1 = 0.5 * X * Y
    
    s = (Z + T + d) / 2
    
    area_triangle2 = math.sqrt(s * (s - Z) * (s - T) * (s - d))
    
    total_area = area_triangle1 + area_triangle2
    
    return total_area

def main():
    X = float(input("Enter the length of side X: "))
    Y = float(input("Enter the length of side Y: "))
    Z = float(input("Enter the length of side Z: "))
    T = float(input("Enter the length of side T: "))
    
    area = area_of_quadrilateral(X, Y, Z, T)
    
    print(f"The area of the quadrilateral is: {area}")

if __name__ == "__main__":
    main()

