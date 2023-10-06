def print_rangoli(size):
    alpha = []
    for i in range(ord('a'), ord('a') + 26):
        alpha.append(chr(i))
    str = []
    for i in range(size):
        s = '-'.join(alpha[size - i - 1:size])
        str.append((s[::-1] + s[1:]).center(size * 4 - 3, '-'))
    result = str + str[:size - 1][::-1]
    print('\n'.join(result))

print_rangoli(3)
print_rangoli(5)
print_rangoli(10)
