def increment_by_one(i):
    return i + 1


def example_exception_handling_without_else():
    number = "Shashi"
    try:
        number = increment_by_one(number)
    except TypeError as te:
        print(te)
    finally:
        print("Finally block executed")

    # multiply by 2 and print
    print(number * 2)


def example_exception_handling_with_else():
    number = 5
    try:
        number = increment_by_one(number)
    except TypeError as te:
        print(te)
    else:
        # multiply by 2 and print
        print(number * 2)
    finally:
        print("Finally block executed")


def main():
    example_exception_handling_without_else()
    example_exception_handling_with_else()


if __name__ == "__main__":
    main()

