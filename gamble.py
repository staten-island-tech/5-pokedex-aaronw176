def slots(quarters, m1, m2, m3):
    x = 0
    m = 1
    while quarters > 0:
        if m == 1 and quarters > 0:
            quarters -= 1
            m1 += 1
            x += 1
            m = 2
            if m1 == 35:
                quarters += 30
                m1 = 0
        if m == 2 and quarters > 0:
            quarters -= 1
            m2 += 1
            x += 1
            m = 3
            if m2 == 100:
                quarters += 60
                m2 == 0
        if m == 3 and quarters > 0:
            quarters -= 1
            m3 += 1
            x += 1
            m = 1
            if m3 == 10:
                quarters += 9
                m3 = 0

    print(f"Martha plays {x} times before going broke")
slots(6.000000001, 4, 9, 3)