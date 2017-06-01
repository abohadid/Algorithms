def bubsort(s):
    l = len(s)
    p = 0
    while p<l:
        for i in range(0,len(s)-1):
            if s[i]>s[i+1]:
                tmp = s[i]
                s[i] = s[i+1]
                s[i+1] = tmp
        l=l-1

    return s
