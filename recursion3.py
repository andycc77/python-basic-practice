def gcd(m, n):
    if n == 0:  # 何時會停止
        return m
    else:
        return gcd(n, m % n)


print(gcd(6, 3))
