def split_and_join(line):
    # split the line into a list of words
    words = line.split(" ")
    # join the words with a hyphen
    hyphenated = "-".join(words)
    # return the hyphenated string
    return hyphenated

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)