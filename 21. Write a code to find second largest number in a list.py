def find_secondlargest(number):
    unique_numbers = list(set(number))
    if len(unique_numbers) < 2:
        return "There is no second largest number in this List"
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]


number_list = list(map(int, input("Enter numbers seperated by space: ").split()))
second_largest = find_secondlargest(number_list)
print(f"Second largest number of List is {second_largest}")