def factorial(n):
    def fact(num, acc):
        if num == 0:
            return acc
        else:
            return fact(num - 1, num * acc)

    return fact(n, 1)


def factorial_v1(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial_v1(n - 1, acc * n)


def main():
    op = factorial(2000)
    print(op)
    op = factorial_v1(5)
    print(op)


if __name__ == '__main__':
    main()
