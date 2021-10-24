inp = 'abcd'
inver = inp[::-1]
if inp == inver:
    print("already a palindrome")
else:
    res = ''
    i = 0
    while i < len(inp):
        if inp[i] != inver[i]:
            inver = inver[:i] + inp[i] + inver[i:]
            res += inp[i]
        else:
            i += 1
    print("min letters required: " +
          res[::-1] + '\n'+"full palindrome: " + inver)
