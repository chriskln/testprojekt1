if __name__ == '__main__':
    s = 'abcdefghiajklm'
    print(len(s))
    print(s[1:5])
    # first 7 letters
    print(s[:7])
    # last 7 letters
    print(s[-7:])
    # chosen letters in a range
    print(s[-7:-4])
    # count number of times a specific letter occurs
    print(s.count('a'))
    # location of letter from beginning
    print(s.index('a'))
    # location of letter from last
    print(s.rindex('a'))

    print('_______________')



