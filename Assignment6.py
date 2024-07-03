def calculate_average(marks):
    try:
        if not marks:
            raise ZeroDivisionError()

        total = 0
        count = 0

        for mark in marks:
            if not isinstance(mark, (int, float)):
                raise ValueError()
            total += mark
            count += 1

        average = total / count
        return average

    except ZeroDivisionError:
        print("Zero Division Error")
    except ValueError as ve:
        print("Value Error")


marks1 = [20, 40, "eighty"]
marks2 = [20, 40, 80]
marks3 = []

calculate_average(marks1)
print("Average of marks2:", calculate_average(marks2))
calculate_average(marks3)
