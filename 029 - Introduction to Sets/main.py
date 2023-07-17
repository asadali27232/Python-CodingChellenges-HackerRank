def average(array):
    my_set = set(array)
    return sum(my_set) / len(my_set)


arr = list(map(int, input().split()))
result = average(arr)
print(result)
