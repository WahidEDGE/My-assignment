import math

input_numbers = input("Enter some numbers separated by spaces: ")
try:
    # Split the input string into a list of strings
    numbers_str_list = input_numbers.split()

    # Convert each string to an integer and store them in a list
    numbers_list = [int(num) for num in numbers_str_list]

    max_numberlit = max(numbers_list)
    minimum_number = min(numbers_list)
    sum_number = sum(numbers_list)
    print("List of numbers:", numbers_list)
    print("Maximum Number Is ", max_numberlit)
    print("Sum of number list is ", sum_number)
    print("Minimum number is", minimum_number)


    def is_prime():
        if num < 2:
            return False
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                return False
        return True


    for num in numbers_list:
        if is_prime():
            print(f"{num} is Prime")

        else:
            print(f"{num} is not prime")
except ValueError:
    print("Number cannot be Alphabet or Symbol")

except Exception as e:
    print("An error occur", e)