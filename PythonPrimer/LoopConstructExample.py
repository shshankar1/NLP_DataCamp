def main():
    for i in range(10):
        print(i)

    numbers = range(10)
    evens = [i for i in numbers if i % 2 == 0]
    print(evens)

    i = 5
    while i > 0:
        print(i)
        i -= 1

    
if __name__ == "__main__":
    main()
