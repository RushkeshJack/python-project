def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_list = [0, 1]
    while len(fibonacci_list) < n:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    return fibonacci_list

n = 10
fibonacci_numbers = generate_fibonacci(n)
print(fibonacci_numbers)
