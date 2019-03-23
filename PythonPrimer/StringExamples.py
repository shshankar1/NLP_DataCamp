def main():
    simple_string = "Hello" + "\t I am simple string"
    print(simple_string)

    multiline_string = """
    Hello
    My name is Shashi
    """

    print(multiline_string)

    escaped_string = "C:\the_folder\new_dir\file.txt"
    print(escaped_string)

    raw_string = r'C:\the_folder\new_dir\file.txt'
    print(raw_string)

    print('Hello' ' and' ' Welcome to Python!!!')

    s2 = "---Python---"
    print(s2 * 5)

    s3 = ('This '
          'is '
          "another way to "
          "concatenate String")
    print(s3)

    print('is' in s3)

    print(len(s3))


if __name__ == "__main__":
    main()
