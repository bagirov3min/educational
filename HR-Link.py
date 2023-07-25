def price_flat(n, m, x):
    a = x * m
    b = 1000
    c = 0

    for _ in range(m, n + 1, m):
        c += a
        a += b * m

    if n % m != 0:
        c += (n % m) * (x + b * (n // m))
    return c


n, m, x = int(input()), int(input()), int(input())
print(price_flat(n, m, x))
