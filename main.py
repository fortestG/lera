f = open('/Users/adored/Downloads/17.txt')
a = [int(i) for i in f]
count = 0
mx = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if ((a[i] + a[j]) % 60 == 0) and ((a[i] % 40 == 0) or (a[j] % 40 == 0)):
            count += 1
            mx = max(mx, a[i] + a[j])
print(count, mx)







