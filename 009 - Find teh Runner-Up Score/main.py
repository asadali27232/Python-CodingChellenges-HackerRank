if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    my_list = list(arr)
    my_set = set(my_list)

    my_set.remove(max(my_set))

    print(max(my_set))
