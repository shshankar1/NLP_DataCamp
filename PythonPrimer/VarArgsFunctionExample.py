def square(*args):
    squared_args = []
    for arg in args:
        squared_args.append(arg * arg)
    return squared_args


def main():
    squared_args = square(1, 2, 3, 4)
    print(squared_args)


if __name__ == "__main__":
    main()
