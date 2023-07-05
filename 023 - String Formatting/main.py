def print_formatted(number):
    print_list = [
        [str(n), oct(n)[2:], hex(n)[2:].upper(), bin(n)[2:]]
        for n in range(1, number + 1)
    ]
    for line in print_list:
        for index, word in enumerate(line):
            width = len(print_list[len(print_list) - 1][3])
            if index == 0:
                print(word.rjust(width), end="")
            else:
                print(word.rjust(width + 1), end="")
        print()


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
