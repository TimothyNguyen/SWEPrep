import re
for _ in range(int(input())):
    if re.match(r'789\d{9}$', input()):
        print('Yes')
    else:
        print('No')