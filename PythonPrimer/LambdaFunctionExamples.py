def main():
    nums = [1, 2, 3, 4, 5, 6]
    squared_nums = map(lambda x: x * x, nums)
    for num in iter(squared_nums):
        print(num)

    even_nums = filter(lambda x: x % 2 == 0, nums)
    for num in iter(even_nums):
        print(num)


if __name__ == "__main__":
    main()
