def print_input(inp):
    return 'The input received is ', inp

if __name__ == '__main__':
    num = input('Enter a number: ')
    print print_input(num)
    s = raw_input('Enter a string: ')
    print print_input(s)
