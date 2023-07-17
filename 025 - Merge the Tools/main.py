def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub_string = string[i:i+k]
        seen = set()
        for i in sub_string:
            if i not in seen:
                print(i, end="")
                seen.add(i)
        print()

string, k = input(), int(input())
merge_the_tools(string, k)