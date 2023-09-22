def solve(s):
    if not s:
        return ""
    newlist = []
    n = s.split()
    dict = {}
    for i in n:
        newlist.append(i[:1].upper() + i[1:].lower())
    for word in newlist:
        dict.update({word.lower():word})
    for key,value in dict.items():
        s = s.replace(key,value)
    return s


print(solve("text     text   65text   text text"))