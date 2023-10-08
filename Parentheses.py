def isValid(s) -> bool:
    dict = {']': '[', ')': '(', '}': '{'}#having the closing value equal to the openning value,

    stack = []#creating a stack that hold the openining of parentheses
    for i in s:
        if i in dict:
            if stack and stack.pop() == dict[i]:#checking the stack is not empty before poping, and then check if value that got popped is equal to the opening
                continue
            else:
                return False
        stack.append(i)
    return not stack

print(isValid('[{{}]'))#returns False
print(isValid('[{}]'))#returns True