num = input("Please input a number: ")
num = [int(x) for x in str(num)]
r = len(num)-1
l = r-1
while r > 0 and l<=r:
    if num[l] < num[r]:
        temp = num[l]
        num[l] = num[r]
        num[r] = temp
        break
    else:
        if l != 0:
            l -= 1
        else:
            r -= 1
            l = r-1
print("".join(str(num1) for num1 in num))
