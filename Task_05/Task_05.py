def find_numbers(n, divisors):
    result = []
    for i in range(1, n + 1):
        if all(i % divisor == 0 for divisor in divisors):
            result.append(i)
    return result

def main():
    n = int(input("Enter the value of n: "))
    
    divisors = list(map(int, input("Enter the divisors separated by spaces: ").split()))
    
    numbers = find_numbers(n, divisors)
    
    print("The numbers that do not exceed", n, "and are divisible by all given divisors are:")
    print(numbers)

if __name__ == "__main__":
    main()

