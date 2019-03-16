import os


def write_file():
    file = open("sample.txt", "w")
    file.write("This is sample text \n")
    file.write("Hello World!! I like Python")
    file.close()


def read_file():
    file = open("sample.txt", "r")
    data = file.readlines()
    for d in data:
        print(d)


def list_files():
    files = os.listdir(os.getcwd())
    print(files)


def main():
    # write_file()
    # read_file()
    list_files()


if __name__ == "__main__":
    main()
