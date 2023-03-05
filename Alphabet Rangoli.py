def print_rangoli(size):
    # create a list of alphabets
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # select the letters to be used in the rangoli
    letters = alphabet[:size]
    # create the top half of the rangoli
    top_half = []
    for i in range(size):
        s = '-'.join(letters[size-i-1:size])
        top_half.append((s[::-1]+s[1:]).center(4*size-3, '-'))
    # create the bottom half of the rangoli
    bottom_half = top_half[::-1]
    # combine the two halves to form the complete rangoli
    complete_rangoli = top_half + bottom_half[1:]
    # print the rangoli
    print('\n'.join(complete_rangoli))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)