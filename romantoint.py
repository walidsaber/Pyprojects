def romanToDecimal(S):
    if not S:
        return 0
    dictt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    summ = 0
    back = 0
    for i in reversed(S):
        num = dictt.get(i, 0)
        if num >= back:
            summ += num
        else:
            summ -= num
        back = num
    return summ
test = 'MMMDCLXXX'
print(romanToDecimal(test))

