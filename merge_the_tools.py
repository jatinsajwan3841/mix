def merge_the_tools(string, k):
    f,l = 0,k
    for _ in range(int(len(string)/k)):
        print(''.join(list(dict.fromkeys(string[f:l]))))
        f += k
        l += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
