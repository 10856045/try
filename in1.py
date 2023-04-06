n = int(input("資料筆數: "))
ans = []

for i in range(n):
    a,b,c,d = list(input("共a張分別為b元與c元的郵票(b<c),共d元: ").strip().split(','))
    
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    x=0
    y=0

    for x in range(0, 100):
        for y in range(0, 100):
            if (x+y) == a:
                if (b*x + c*y) == d:
                    ans.append(str(x) + "," + str(y))

for j in range(n):
    print(ans[j])