import time
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n
def permu(arr):
    if not arr:
        return []
    elif len(arr) == 1:
        return [arr]

    l = []
    for i in range(len(arr)):
        x = arr[i]
        others = arr[:i] + arr[i+1:]
        for p in permu(others):
            l.append([x] + p)
    return l


arr = ['A','B','C']
listt = permu(arr)
x = 1
print(f"\t{'='*20}\n\t\tPermutations\n\t{'='*20}\n\nThe User input is  = {arr}\nResult length = {factorial(len(arr))}\n")

for perm in listt:
    print(f"The {x} case is = {perm}",end='\n')
    x += 1
    time.sleep(0.5)


