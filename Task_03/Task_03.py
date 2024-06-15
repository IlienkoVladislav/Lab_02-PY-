def is_point_inside_circle(x, y, a, b, R):
    """
    Checks if the point (x, y) is inside the circle with center (a, b) and radius R.
    """
    distance_squared = (x - a)**2 + (y - b)**2
    return distance_squared < R**2

def main():
    a = float(input("Enter the x-coordinate of the circle's center (a): "))
    b = float(input("Enter the y-coordinate of the circle's center (b): "))
    R = float(input("Enter the radius of the circle (R): "))
    
    p1, p2 = map(float, input("Enter the coordinates of point P (p1 p2): ").split())
    f1, f2 = map(float, input("Enter the coordinates of point F (f1 f2): ").split())
    l1, l2 = map(float, input("Enter the coordinates of point L (l1 l2): ").split())
    
    points_inside = 0
    
    if is_point_inside_circle(p1, p2, a, b, R):
        points_inside += 1
    if is_point_inside_circle(f1, f2, a, b, R):
        points_inside += 1
    if is_point_inside_circle(l1, l2, a, b, R):
        points_inside += 1
    
    print(f"Number of points inside the circle: {points_inside}")

if __name__ == "__main__":
    main()

