str1 = input()
str2 = input()
d = [[0] * 1001 for _ in range(1001)]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i][j-1], d[i-1][j])
print(d[len(str1)-1][len(str2)-1])


