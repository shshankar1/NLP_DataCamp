def main():
    print("Hello %s" % ('Python!!'))

    s = "We have %d %s containing %.2f gallons of %s" % (2, 'bottles', 2.5, 'milk')
    print(s)

    s = 'Hello {} {}, it is a great {} to meet you'.format('Mr.', 'Jones', 'pleasure')
    print(s)

    s = 'I have a {food_item} and a {drink_item} with me.'.format(drink_item='juice', food_item='samosa')
    print(s)


if __name__ == "__main__":
    main()
