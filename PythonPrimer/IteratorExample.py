def main():
    nums = [1, 2, 3, 4, 5, 6]
    itr = iter(nums)
    while True:
        try:
            print(next(itr))
        except StopIteration:
            print("reached end of iterations")
            break


if __name__ == "__main__":
    main()
