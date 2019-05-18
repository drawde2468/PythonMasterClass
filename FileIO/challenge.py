with open("sample.txt", 'a') as times_tables:
    for i in range(1, 13):
        for j in range(1, 13):
            print("{a:2} X {b:2} = {c:3}".format(a=i, b=j, c=i * j), file=times_tables)
        print("-" * 40, file=times_tables)
