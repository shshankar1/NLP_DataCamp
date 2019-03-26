import re


def main():
    s = u'H\u00e8llo'
    print(s)

    result = re.findall(r'\w+', s)
    print(result)

    result = re.findall(r'\w+', s, re.UNICODE)
    print(result)

    pattern = 'python'
    s1 = 'Python is an excellent language'
    s2 = 'I love the Python language. I also use Python to build applications at work!'

    output = re.match(pattern, s1)
    print(output)

    output = re.match(pattern, s1, flags=re.IGNORECASE)
    print(output.group(0))

    output = re.search(pattern, s2, flags=re.IGNORECASE)
    print('Found match {} ranging from index {} - {} in the string "{}"'
          .format(output.group(0), output.start(), output.end(), s2))

    output = re.findall(pattern, s2, flags=re.IGNORECASE)
    print(output)


if __name__ == '__main__':
    main()
