my_string = "Sorting1234"

numbers = [int(number) for number in my_string if number.isdigit()]
numbers = sorted(numbers, key=lambda item: item % 2 == 0)

lower_letters = [letter for letter in my_string if not letter.isdigit() and letter.islower()]
upper_letters = [letter for letter in my_string if not letter.isdigit() and letter.isupper()]

lower_letters = sorted(lower_letters)
upper_letters = sorted(upper_letters)

result = lower_letters + upper_letters + numbers

print(*result)