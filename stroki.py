a = [ 'b','da', 'c', 'ddd', 'na', 'a']
count = 0
for i in a:
    if len(i) == 10:
        count += 1
        print('da')
        break
if count == 0:
    print('ne')

