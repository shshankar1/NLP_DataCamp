def generate_square(numbers):
    for num in numbers:
        yield num * num


def main():
    # example 1
    numbers = [1, 2, 3, 4, 5]
    gen_obj = generate_square(numbers)
    for item in gen_obj:
        print(item)

    # example 2
    csv_string = "The,fox,jumps,over,the,dog"
    gen_obj = (item for item in csv_string.split(","))
    print(" ".join(gen_obj))


if __name__ == "__main__":
    main()
