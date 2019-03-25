def main():
    s = 'Python is great'
    print(s.capitalize())
    print(s.upper())
    s = s.replace("Python", 'Analytics')
    print(s)

    s = "This,is,a,comma,seperated,string"
    print(s.split(","))


if __name__ == "__main__":
    main()
