def main():
    # List comprehension to compute squares
    numbers = range(6)
    squared_numbers = [i * i for i in numbers]
    print(squared_numbers)

    # List comprehension to check if number divisible by 2
    even_numbers = [i % 2 == 0 for i in numbers]
    print(even_numbers)

    # Set comprehension to get distinct values
    ages = [23, 45, 23, 30, 67, 32]
    distinct_ages = set(i for i in ages)
    print(distinct_ages)

    # dictionary comprehension for number and its square
    sqaure_dict = {i: i * i for i in range(10)}
    print(sqaure_dict)

    # complex comprehension using list and dictionary
    comp = [
        {"number": num,
         "square_num": num * num,
         "type": "even" if num % 2 == 0 else "odd"
         } for num in range(10)]
    print(comp)

    # list comprehension for flattening
    list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat_list = [item for each_list in list_of_list for item in each_list]
    print(flat_list)


if __name__ == "__main__":
    main()
