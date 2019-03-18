def person_details(**kwargs):
    for key, value in kwargs.items():
        print(key, "->", value)


def main():
    person_details(name='James Bond', alias='007')


if __name__ == '__main__':
    main()
